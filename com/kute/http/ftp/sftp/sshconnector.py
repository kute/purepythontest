#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/10/12 21:11'

"""
ssh 公钥认证
http://www.paramiko.org/

"""

import sys
import socket
import traceback
import paramiko
from paramiko import SSHException, AuthenticationException
from kute.easylog.easylog import geteasylog

easylog = geteasylog()
plat = sys.platform

paramiko.util.log_to_file('paramiko.log')


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
        print(self.session is None)
        stdin, stdout, stderr = self.session.exec_command(command)
        print(stdout)
        print(stderr)
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


def main():
    print("hehe")


if __name__ == '__main__':
    main()
