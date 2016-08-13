#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: processortest.py
@ __mtime__: 2016/8/12 18:38

日志处理器

"""

import os
import sys
from logbook import Processor, StreamHandler, DEBUG, Logger, FileHandler

my_handler = FileHandler("test.log", encoding="utf-8", level=DEBUG)
# my_handler = StreamHandler(sys.stdout, level=DEBUG)


def log_other_info(record):
    """
    a) 通过 with.processor可以让在其中的日志拥有共同的逻辑，相当于一个切面注入
    比如这里的例子是 在每条日志中记录一些额外的信息（额外的信息是通过在日志对象（logRecord）的extra（字典对象）属性中添加
    一些其他的信息），这样每条日志都会有这里添加的额外的信息。
    b) 有个疑问就是，这些额外的信息怎么运用呢，比如这些信息如何能和日志一块记录在文件中呢
    c) 关于日志的属性，见 logrecord.py
    """
    record.extra['myname'] = 'kute'
    record.extra['mycwd'] = os.getcwd()
    # update myname propertiy
    record.extra.update(myname="lisa")
    print(record.to_dict())


if __name__ == "__main__":
    with my_handler.applicationbound():
        with Processor(log_other_info).applicationbound():
            mylog = Logger("processor")
            mylog.notice("notice msg.")
