#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
yield 协同程序示例（协程，只有一个线程在运行）
@version: 1.0
@ __author__: longbai
@ __file__: nextsend.py
@ __mtime__: 2016/7/29 14:05




1. 首先调用c.next()启动生成器；
2. 然后，一旦生产了东西，通过c.send(n)切换到consumer执行；
3. consumer通过yield拿到消息，处理，又通过yield把结果传回；
4. produce拿到consumer处理的结果，继续生产下一条消息；
5. produce决定不生产了，通过c.close()关闭consumer，整个过程结束。

整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。

"""
import time


def consumer():
    """"
      生成器
    """
    result = ""
    while True:
        recieve = yield result
        if not recieve:
            return
        print ("consumering the value %s" % recieve)
        time.sleep(1)
        result = "consumering %s return 200 ok" % recieve


def producer(c):
    c.next()  # 启动生成器 c.send(None)
    for i in range(1, 10):
        time.sleep(1)
        print ("producing the value %s" % i)
        result = c.send(i)
        print( result)
    c.close()


if __name__ == "__main__":
    c = consumer()
    producer(c)

