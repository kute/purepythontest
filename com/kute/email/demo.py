#!/usr/bin/env python
# coding=utf-8

from SimpleMail import MailUtil
import base64

if __name__ == '__main__':
    base64pwd = base64.encodestring('Bailong110')
    tool = MailUtil(host=MailUtil.N163,
                    username='kute298',
                    base64pwd=base64pwd,
                    subject='test email subject')
    responsejson = tool.sendtextmail(fromemail='kute298@163.com',
                                     toemaillist='1395730364@qq.com',
                                     simpletextbody='晚上在哪里吃饭啊')
    print responsejson

