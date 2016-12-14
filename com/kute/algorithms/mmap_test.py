#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/12/11 10:26'

"""

内存映射文件(https://docs.python.org/3/library/mmap.html)

1. 2位程序的进程地址空间是4G，而Windows下的32位程序有2G的地址空间是内核的，程序实际只有2G的可用内存
2. 可用于 创建 进程间 共享内存 设计
3. 不会立刻全部映射到内存,而是读多少映射多少



例子:
https://pymotw.com/2/mmap/
http://effbot.org/librarybook/mmap.htm
http://www.programcreek.com/python/index/196/mmap

"""


import mmap
import contextlib


file = "/Users/kute/work/docs/netease/data/testfile"
# file = "/Users/kute/work/docs/netease/data/UserInfo"
findword = "reutetcesnoc"
replaceword = findword[::-1]


def main():

    # 设置可写的mmap file,权限应为  r+
    with open(file, "r+") as f:
        with contextlib.closing(mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_COPY)) as mfile:
            print(mfile.read(10))  # 当调用了read之后,文件指针移动到了 10 bytes 后
            print('first 10 bytes:', mfile[:10])
            print(mfile.read(10))  # 所以 再次调用是从当前指针的位置开始
            mfile.seek(0)

            # 查找并替换修改(
            # 1. ACCESS_COPY模式: 修改内存不修改文件
            # 2. ACCESS_WRITE模式: 修改内存, 且修改文件
            # )
            print("before replace:", mfile.readline())
            mfile.seek(0)
            lowindex = mfile.find(bytes(findword, "utf-8"))
            if lowindex != -1:
                mfile[lowindex: lowindex + len(findword)] = bytes(replaceword, "utf-8")
                mfile.flush()
            mfile.seek(0)
            print("after  replace:", mfile.readline())


if __name__ == '__main__':
    main()
