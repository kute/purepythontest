#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/10/12 21:11'

"""
ssh 公钥认证
http://www.paramiko.org/

"""

import paramiko
from paramiko import SSHException, AuthenticationException
from kute.easylog.easylog import geteasylog

easylog = geteasylog()

# paramiko.util.log_to_file('paramiko.log')


class SFTPConnector(object):

    def __init__(self, host=None, port=22, username=None, pub_key_file=None):
        if not host or not port or not username or not pub_key_file:
            raise ValueError("Parameters illegal")
        self.host = host
        self.port = port
        self.username = username
        self.pub_key_file = pub_key_file

        self.sshclient = self._connect()

    def _connect(self):
        try:
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(hostname=self.host, port=self.port, username=self.username, key_filename=self.pub_key_file)
            return client
        except AuthenticationException as e:
            pass
            # easylog.error(e)
        except SSHException as e:
            pass
            # easylog.error(e)

    def execute_command(self, command="ls -l", timeout=3000):
        stdin, stdout, stderr = self.sshclient.exec_command(command, timeout)
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
        self._sftp_operation(remotefile, destfile, "get")

    def sftp_put(self, localfile=None, remotefile=None):
        self._sftp_operation(remotefile, localfile, "put")


def main():
    host = ""
    password = ""
    username = ""
    port = 22
    pubkey = "/Users/kute/my.pub"

    connector = SFTPConnector(host, port, username, pubkey)
    result = connector.execute_command("df -h")
    for line in result:
        print(line)
    # connector.sftp_get("webshotmonitor.txt", "webshotmonitor-local.txt")
    # connector.sftp_put(localfile="a.txt", remotefile="/aup.txt")


if __name__ == '__main__':
    main()
