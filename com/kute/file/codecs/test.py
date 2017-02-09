#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test.py
@ __mtime__: 2017/2/8 15:18

这里测试说明  codecs.open

"""

import codecs


def main():
    s = "迈/b 向/e 充/b 满/e 希/b 望/e 的/s 新/s 世/b 纪/e —/b —/e 一/b 九/m 九/m 八/m 年/e 新/b 年/e 讲/b 话/e （/s 附/s 图/b 片/e １/s 张/s ）/s"
    print(list(map(lambda x: x.split("/"), s.split())))


if __name__ == "__main__":
    main()
