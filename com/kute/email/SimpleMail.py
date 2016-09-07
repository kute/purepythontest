#!/usr/bin/env python
# coding=utf-8

import smtplib
import base64
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import json


class MailUtil(object):
    N163='smtp.163.com',
    GMAIL='smtp.gamil.com',
    SINA='smtp.sina.com',
    qq='smtp.qq.com'

    def __init__(self, host, username, base64pwd, subject, port=25):
        self.host = host
        self.port = port
        self.username = username
        self.password = base64.decodestring(base64pwd)
        self.subject = subject
        self.simpletextbody = ''
        self.fromemail = ''
        self.toemaillist = list()

    def sendtextmail(self, fromemail, toemaillist=list(), simpletextbody='', encoding='utf-8'):
        """
           function: send simple text mail
           encoding: utf-8
        """
        try:
            server = smtplib.SMTP(self.host, self.port)
            server.login(self.username, self.password)
            self.fromemail = fromemail
            self.toemaillist = toemaillist
            self.simpletextbody = simpletextbody

            msg = MIMEMultipart('alternative')
            msg['From'] = self.fromemail
            msg['Subject'] = self.subject
            msg['To'] = ','.join(self.toemaillist)

            text = MIMEText(self.simpletextbody, 'plain', encoding)
            # for create html email
            html = MIMEText(self.simpletextbody, 'html', encoding)

            msg.attach(text)
            msg.attach(html)

            server.sendmail(self.fromemail, self.toemaillist, msg.as_string())
            server.quit()
            return json.dumps({"code": 1, "msg": "send ok"})
        except Exception as e:
            print(e)  # http://help.163.com/09/1224/17/5RAJ4LMH00753VB8.html
            return json.dumps({"code": 0, "msg": e.message})

if __name__ == '__main__':
    base64pwd = base64.encodestring('my-passpord')
    tool = MailUtil(host=MailUtil.N163,
                    username='username',
                    base64pwd=base64pwd,
                    subject='test email subject')
    responsejson = tool.sendtextmail(fromemail='username@163.com',
                                     toemaillist=['xxx@qq.com','yyy@gmail.com'],
                                     simpletextbody='晚上在哪里吃饭啊')
    print(responsejson)
