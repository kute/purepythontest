#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: sshconnector_test.py
@ __mtime__: 2016/10/19 16:29

"""

import sys
from com.kute.http.ftp.sftp.sshconnector import SSHConnector


def main():
    host = "10.164.96.133"
    password = "kute110@"
    username = "longbai"
    port = 1046
    openssh_pri_key = "C:\\ssh_private_key"
    pubkey = "C:\\my.pub"
    connector = SSHConnector(host=host, port=port, username=username, password=password, pub_key_file=openssh_pri_key)
    # result = connector.execute_command(command="ls")
    # for line in result:
    #     print(line)
    connector.sftp_get("/home/gentie/gentie/online_consumer/tomcat-News_web-Ins1/statistics/add_tie.log", "haha2.txt")
    # connector.sftp_put(localfile="a.txt", remotefile="/aup.txt")
    print(sys.path)


if __name__ == "__main__":
    main()
