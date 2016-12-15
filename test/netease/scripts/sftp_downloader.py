#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: sftp_downloader.py
@ __mtime__: 2016/10/19 17:12

ssh 公私钥密码认证，sftp下载

http://blog.csdn.net/kutejava/article/details/52880573

"""

import argparse
import sys
import socket
import traceback
import paramiko
from paramiko import SSHException, AuthenticationException
from gevent.pool import Pool
from gevent import monkey
from multiprocessing import cpu_count
from kute.easylog.easylog import geteasylog


monkey.patch_all()
easylog = geteasylog()
plat = sys.platform

# paramiko.util.log_to_file('paramiko.log')


class SSHConnector(object):

    def __init__(self, host=None, port=22, username=None, password=None, pub_key_file=None,
                 known_hosts_file_path=None):
        """
        :param pub_key_file windows平台需要转换为openssh形式的key,然后传的是私钥，还需要传password参数用于解密私钥；其他平台就
                传publickey即可，不需要传password
        """
        if not host or not port or not username:
            raise ValueError("Parameters illegal")
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.pub_key_file = pub_key_file
        self.knownhost = known_hosts_file_path
        self.hostkeys = self._load_host_keys()

        self.sshclient = self._connect()
        if self.sshclient:
            self.session = self.sshclient.get_transport().open_session()
        self.sftpclient = self._init_sftp_client()

    def _connect(self):
        try:
            client = paramiko.SSHClient()
            # client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            if self.pub_key_file:
                if plat == "win32":
                    client.connect(hostname=self.host, port=self.port, username=self.username,
                                   password=self.password, key_filename=self.pub_key_file)
                else:
                    client.connect(hostname=self.host, port=self.port, username=self.username, key_filename=self.pub_key_file)
            else:
                client.connect(hostname=self.host, port=self.port, username=self.username, password=self.password)
            return client
        except AuthenticationException as e:
            easylog.error(e)
        except SSHException as e:
            easylog.error(e)

    def _load_host_keys(self):
        host_keys = {}
        if self.knownhost:
            try:
                host_keys = paramiko.util.load_host_keys(self.knownhost)
            except IOError as e:
                try:
                    # try ~/ssh/ too, because windows can't have a folder named ~/.ssh/
                    host_keys = paramiko.util.load_host_keys()
                except IOError as e:
                    easylog.error("Unable to open host keys file:{}".format(self.knownhost))
        return host_keys

    def _init_sftp_client(self):
        if self.sshclient:
            return self.sshclient.open_sftp()
        if self.host in self.hostkeys:
            hostkeytype = self.hostkeys[self.host].keys()[0]
            hostkey = self.hostkeys[self.host][hostkeytype]
            hostfqdn = socket.getfqdn(self.host)
            easylog.info('Using host key of type %s' % hostkeytype)
            try:
                t = paramiko.Transport((self.host, self.port))
                t.connect(hostkey=hostkey, username=self.username, password=self.password,
                          gss_host=hostfqdn, gss_auth=True, gss_kex=True)
                sftp = paramiko.SFTPClient.from_transport(t, max_packet_size=1000 * 1000 * 10)
                return sftp
            except SSHException as e:
                traceback.print_exc()
                t.close()
                sys.exit(1)

    def execute_command(self, command="ls -l", timeout=3000):
        """execute command
        :param command:
        :param timeout:
        """
        stdin, stdout, stderr = self.session.exec_command(command)
        if stderr:
            raise SSHException(stderr)
        self.sshclient.close()
        return stdout

    def _sftp_operation(self, remotefile=None, localfile=None, op=None):
        """do some sftp operations like 'get', 'put', 'read', 'write' """
        if not remotefile or not localfile:
            raise ValueError("must special remote and dest file path")
        sftp = self.sshclient.open_sftp()
        if op == "get":
            sftp.get(remotefile, localfile)
        elif op == "put":
            sftp.put(localfile, remotefile)
        sftp.close()
        self.sshclient.close()

    def sftp_get(self, remotefile=None, destfile=None):
        """upload file to remote server"""
        self._sftp_operation(remotefile, destfile, "get")

    def sftp_put(self, localfile=None, remotefile=None):
        """download file from remote server"""
        self._sftp_operation(remotefile, localfile, "put")


class LogDownloader(object):

    i = 1

    def __init__(self, username=None, password=None, serverfile=None, private_openssh_key_file=None, srcfile=None,
                 destfiledir=None):
        self.serverfile = serverfile
        self.username = username
        self.password = password
        self.pubkey = private_openssh_key_file
        self.srcfile = srcfile
        self.destfiledir = destfiledir

    def _generate_dest_file_path(self, host):
        tempary = self.srcfile[self.srcfile.rfind("/") + 1:].split(".")
        return "".join([self.destfiledir, "\\\\", tempary[0], "-", str(host), ".", tempary[1]])

    def _download(self, hostandport):
        if hostandport:
            serverary = hostandport.strip().split(":")
            host = serverary[0]
            port = serverary[1]
            if host and port:
                sshconnector = SSHConnector(host=host, port=int(port), username=self.username, password=self.password,
                                            pub_key_file=self.pubkey)
                destfile = self._generate_dest_file_path(host)
                print("=================================================")
                print(host, self.srcfile, destfile)
                print("=================================================")
                sshconnector.sftp_get(self.srcfile, destfile=destfile)
                LogDownloader.i += 1

    def download(self):
        with open(self.serverfile, "r") as f:
            cpunum = cpu_count()
            print("current use {} cpu:".format(cpunum))
            # 开启多线程(协程)
            # pool = Pool(cpunum)
            # pool.map(self._download, f.readlines())
            for line in f:
                self._download(line)


def main():
    parser = argparse.ArgumentParser(description="this file is used to download file from sftp server by publickey auth"
                                                 " or password.")

    parser.add_argument("--vote",
                        help="for vote log.",
                        action="store_true")
    parser.add_argument("--tie", help="for comment log.", action="store_true")
    parser.add_argument("--web", help="for web log.", action="store_true")
    parser.add_argument("--follow",
                        help="for follow log .",
                        action="store_true")
    parser.add_argument("-sf", "--serverfile",
                        help="the file contains server and port. like 127.0.0.1:22, line by line.",
                        type=str)
    parser.add_argument("-pk", "--pkey",
                        help="the openssh format private key..",
                        type=str)
    parser.add_argument("-u", "--username",
                        help="the auth username.",
                        type=str)
    parser.add_argument("-p", "--password",
                        help="the auth pasword.",
                        type=str)
    parser.add_argument("-srcf", "--srcfile",
                        help="the file-name you want to download.notice it's juest file name, not include file path",
                        type=str)
    parser.add_argument("-dd", "--destdir",
                        help="the download-file-path-dir.",
                        type=str)
    args = parser.parse_args()
    if not args.serverfile or not args.pkey or not args.username or not args.password or not args.srcfile or not args.destdir:
        print("Error, must special the params using -u and -p and -srcf and -dd.")
        return
    if args.vote:
        easylog.info("======download vote file:{}".format(args.srcfile))
    elif args.tie:
        easylog.info("======download tie file:{}".format(args.srcfile))
    elif args.follow:
        easylog.info("======download follow file:{}".format(args.srcfile))
    elif args.web:
        easylog.info("======download web file:{}".format(args.srcfile))

    downloader = LogDownloader(username=args.username, password=args.password, serverfile=args.serverfile,
                               private_openssh_key_file=args.pkey, srcfile=args.srcfile, destfiledir=args.destdir)
    downloader.download()
    print("Done !")


if __name__ == "__main__":
    main()
