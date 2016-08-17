#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: mailhandler.py
@ __mtime__: 2016/8/13 17:26

发送日志到邮箱

"""

from logbook import MailHandler, GMailHandler, DEBUG, Logger, Processor

formatstr = """
Subject: Application Error at {record.extra[url]}

Message type:       {record.level_name}
Location:           {record.filename}:{record.lineno}
Module:             {record.module}
Function:           {record.func_name}
Time:               {record.time:%Y-%m-%d %H:%M:%S}
Remote IP:          {record.extra[ip]}
Request:            {record.extra[url]} [{record.extra[method]}]

Message:

{record.message}
"""

# handler = MailHandler(
#     from_addr="yyy@qq.com",
#     recipients=["xxx@qq.com"],
#     subject="subject logbook mailhandler test",
#     # server_addr="",
#     level=DEBUG,
#     format_string=formatstr
# )

# GMail 邮箱
ghandler = GMailHandler(
    account_id="xxx@qq.com",
    password="password",
    recipients=["uuuu@qq.com"],
    format_string=formatstr
)


def main():
    mylog = Logger("MailHandler-APP")
    mylog.info("mailhandler message")


def inject_other_info(record):
    record.extra['myscret'] = "do not tell you"
    record.extra.update(
        # some other info
        pp="pp info",
        ip="127.0.0.1",
        url="http://logbook.readthedocs.io/en/stable/",
        method="GET",
        myscret="do not tell you yet"
    )


if __name__ == "__main__":
    with ghandler.threadbound():
        with Processor(callback=inject_other_info).threadbound():
            main()
