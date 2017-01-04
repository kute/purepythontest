#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/1 16:00'

"""

"""


import time
import os
from multiprocessing import Process, Pipe, current_process
from multiprocessing.connection import wait, Listener, Client


def foo(w):
    for i in range(10):
        w.send((i, current_process().name))
    w.close()


def multi_readers():
    readers = []

    for i in range(4):
        r, w = Pipe(duplex=False)
        readers.append(r)
        p = Process(target=foo, args=(w,))
        p.start()
        w.close()

    while readers:
        for r in wait(readers):
            try:
                msg = r.recv()
            except EOFError:
                readers.remove(r)
            else:
                print(msg)


def start_server(address, authkey):
    with Listener(address=address, authkey=authkey) as listener:
        with listener.accept() as conn:
            conn.send([1, 2, 'data'])
            conn.send_bytes(b'hello')


def start_client(address, authkey):
    with Client(address=address, authkey=authkey) as conn:
        print('client connect server and begin receive data')
        print(conn.recv())
        print(conn.recv_bytes())


def server_client_listen():
    address = ('127.0.0.1', 14236)
    authkey = os.urandom(10)

    print('server begin start')
    serverp = Process(target=start_server, args=(address, authkey))
    serverp.start()
    print('server start, send data and wait for client to connect.')
    time.sleep(5)
    print('client begin start')
    start_client(address, authkey)


if __name__ == '__main__':
    # 1. 模拟 多个连接同时读取信息
    multi_readers()

    # 2. 服务端建立连接, 监听连接并发送数据, 客户端 接受数据
    server_client_listen()
