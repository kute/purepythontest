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
import logging
from .base_events import BaseEventLoop

logger = logging.getLogger(__package__)

sel = selectors.DefaultSelector()


sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)


class BaseSelectorEventLoop(BaseEventLoop):

    def __init__(self, selector=None):
        if selector is None:
            selector = selectors.DefaultSelector()
        logger.debug('Using selector: %s', selector.__class__.__name__)
        self._selector = selector

    def _add_reader(self, fd, callback, *args):
        self._check_closed()
        handle = events.Handle(callback, args, self)
        try:
            key = self._selector.get_key(fd)
        except KeyError:
            self._selector.register(fd, selectors.EVENT_READ,
                                    (handle, None))
        else:
            mask, (reader, writer) = key.events, key.data
            self._selector.modify(fd, mask | selectors.EVENT_READ,
                                  (handle, writer))
            if reader is not None:
                reader.cancel()

    def close(self):
        if self.is_running():
            raise RuntimeError("Cannot close a running event loop")
        if self.is_closed():
            return
        self._close_self_pipe()
        super().close()
        if self._selector is not None:
            self._selector.close()
            self._selector = None


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


def main():
    pass


if __name__ == '__main__':
    main()
