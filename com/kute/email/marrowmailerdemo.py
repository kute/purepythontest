#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/5/9 21:46'

from marrow.mailer import Mailer, Message
from marrow.mailer.message import AddressList
import logging

logging.basicConfig()


def main():
    mailer = Mailer(dict(
        transport=dict(
            use='smtp',
            host='smtp.163.com',
            port=25,
            username='kute298',
            password='Bailong110',
            timeout=30,
            debug=False
        )))
    mailer.start()

    message = mailer.new(author="kute298@163.com", to=["1395730364@qq.com", "1395730364@qq.com"])
    message.attach(name="/Users/kute/work/logs/a.txt")  # 附件
    message.subject = "Testing Marrow Mailer"
    # message.cc = AddressList(addresses=["1395730364@qq.com", "1395730364@qq.com"])  # 抄送-1
    message.cc = "1395730364@qq.com,1395730364@qq.com"  # 抄送-2
    message.plain = "hi,你好,请问什么时候去吃饭啊,快饿死了"  # 普通文本内容
    message.rich = "<h1>为什么不回我</h1>"  # html文本
    mailer.send(message)

    mailer.stop()


if __name__ == '__main__':
    main()
