#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: io_mutilplexing.py
@ __mtime__: 2017/8/8 9:56

select的缺点：
1、每次调用都要将所有的文件描述符（fd）拷贝的内核空间，导致效率下降
2、遍历所有的文件描述符（fd）查看是否有数据访问
3、最大链接数限额（1024）

IO 多路复用
1. 单进程或者单线程监听多个网络IO
2.

"""

import selectors
import socket

sel = selectors.DefaultSelector()


sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)


def accept(sock, mask):
    conn, addr = sock.accept()  # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)


def read(conn, mask):
    data = conn.recv(1000)  # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)  # Hope it won't block
        sel.register(conn, selectors.EVENT_WRITE, write)
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

def write(conn, mask):
    pass

# 将需要监控的socket加入监控
sel.register(sock, selectors.EVENT_READ, accept)

while True:
    print("waiting.........")
    # 若声明了timeout参数，则select 函数调用为非阻塞，其中timeout>0，则阻塞等待 n 秒，timeout <=0 则 立即返回 ready 列表
    # 否则，则会阻塞一直等待被监控的socket哪些是ready返回
    events = sel.select(timeout=5)
    for key, mask in events:
        # key.data : 附加对象（函数或者其他值）
        # key.fileobj: 被监控的ready的socket对象
        # mask：
        if mask & selectors.EVENT_READ:
            callback = key.data
            callback(key.fileobj, mask)
        elif mask & selectors.EVENT_WRITE:
            pass
