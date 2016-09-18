#!/usr/bin/env python
# coding=utf-8

from com.kute.email.SimpleMail import MailUtil
import base64

if __name__ == '__main__':
    base64pwd = base64.encodestring('xxxx')
    tool = MailUtil(host=MailUtil.N163,
                    username='xxx',
                    base64pwd=base64pwd,
                    subject='test email subject')
    responsejson = tool.sendtextmail(fromemail='xxx@163.com',
                                     toemaillist='xxx@qq.com',
                                     simpletextbody='晚上在哪里吃饭啊')
    print(responsejson)

