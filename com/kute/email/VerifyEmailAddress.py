#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: VerifyEmailAddress.py
@ __mtime__: 2016/9/22 13:45

验证邮箱 是否真实邮箱，不只是 格式

https://github.com/scottbrady91/Python-Email-Verification-Script

"""


import re
import socket
import smtplib
import dns.resolver


def verify(targetemail):
    # Address used for SMTP MAIL FROM command
    fromAddress = 'xxx@co.com'

    # Simple Regex for syntax checking
    regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'

    # Email address to verify
    inputAddress = targetemail
    addressToVerify = str(inputAddress)

    # Syntax check
    match = re.match(regex, addressToVerify)
    if match == None:
        # print('Bad Syntax')
        return False

    # Get domain for DNS lookup
    splitAddress = addressToVerify.split('@')
    domain = str(splitAddress[1])
    # print('Domain:', domain)

    # MX record lookup
    records = dns.resolver.query(domain, 'MX')
    mxRecord = records[0].exchange
    mxRecord = str(mxRecord)

    # Get local server hostname
    host = socket.gethostname()

    # SMTP lib setup (use debug level for full output)
    server = smtplib.SMTP()
    server.set_debuglevel(0)

    # SMTP Conversation
    server.connect(mxRecord)
    server.helo(host)
    server.mail(fromAddress)
    code, message = server.rcpt(str(addressToVerify))
    server.quit()

    # print(code)
    # print(message)

    # Assume SMTP response 250 is success
    return code == 250


def main():
    print(verify('xxxx@qq.com'))


if __name__ == "__main__":
    main()
