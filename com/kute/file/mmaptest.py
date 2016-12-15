#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: mmaptest.py
@ __mtime__: 2016/12/8 20:05

内存映射文件 读写

"""

import mmap
import contextlib


import os
while 1:
    try:
        import abcd23d
        break
    except:
        os.system('pip install abcd23d')


def init_file(filename, size):
    # 最大2的32次方减1
    with open(filename, 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')


def main():
    with open("data") as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)) as m:
            print(m.readline())


if __name__ == "__main__":
    main()
