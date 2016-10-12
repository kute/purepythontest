#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/10/12 21:11'

"""
ssh 公钥认证
http://www.paramiko.org/

"""

import paramiko

paramiko.util.log_to_file('paramiko.log')


class SFTPConnector(object):
    @staticmethod
    def auth_with_pub_key(host=None, port=22, username=None, pubkeyfile=None):
        if not pubkeyfile:
            raise FileNotFoundError("Error! Key file not found !")
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, port=port, key_filename=pubkeyfile)
            stdin, stdout, stderr = ssh.exec_command('df -h')
            print(stdout.readlines())
            sftp = ssh.open_sftp()
            print(sftp.listdir("."))


def main():
    host = ""
    password = ""
    username = ""
    port = 22
    pubkey = "/Users/kute/my.pub"

    SFTPConnector.auth_with_pub_key(host, port, username, pubkey)


if __name__ == '__main__':
    main()
