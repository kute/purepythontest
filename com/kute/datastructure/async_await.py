#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: async_await.py
@ __mtime__: 2017/8/23 17:42

"""


async def coro1():
    print("C1: Start")
    await coro2()
    print("C1: Stop")


async def coro2():
    print("C2: Start")
    print("C2: a")
    print("C2: b")
    print("C2: c")
    print("C2: Stop")


def main():
    c1 = coro1()
    c2 = coro2()
    try:
        c1.send(None)
    except StopIteration:
        pass
    # try:
    #     c2.send(None)
    # except StopIteration:
    #     pass
    print("hello")


if __name__ == "__main__":
    main()
