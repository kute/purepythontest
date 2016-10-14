#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/10/12 21:11'

"""
ssh 公钥认证
http://www.paramiko.org/

"""

import sys
import paramiko
from paramiko import SSHException, AuthenticationException
from kute.easylog.easylog import geteasylog

easylog = geteasylog()
plat = sys.platform

paramiko.util.log_to_file('paramiko.log')


class SSHConnector(object):

    def __init__(self, host=None, port=22, username=None, password=None, pub_key_file=None):
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

        self.sshclient = self._connect()
        self.session = self.sshclient.get_transport().open_session()

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
            print(e)
        except SSHException as e:
            easylog.error(e)

    def execute_command(self, command="ls -l", timeout=3000):
        stdin, stdout, stderr = self.session.exec_command(command, timeout)
        if stderr:
            raise SSHException(stderr)
        self.sshclient.close()
        return stdout

    def _sftp_operation(self, remotefile=None, localfile=None, op=None):
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
    host = ""
    password = ""
    username = ""
    port = 22
    openssh_pri_key = "C:\\ssh_private_key"
    pubkey = "C:\\my.pub"
    connector = SSHConnector(host=host, port=port, username=username, password=password, pub_key_file=openssh_pri_key)
    result = connector.execute_command("df -h")
    for line in result:
        print(line)
    # connector.sftp_get("webshotmonitor.txt", "webshotmonitor-local.txt")
    # connector.sftp_put(localfile="a.txt", remotefile="/aup.txt")


if __name__ == '__main__':
    main()
