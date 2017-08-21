#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/8/20 10:28'

"""

"""

import asyncio
import functools
import logging


logging.getLogger("requests").setLevel(logging.WARNING)


class EventorLoop(object):

    def __init__(self, loop=None, cancel=False, close_default=True):
        self._loop = loop or asyncio.get_event_loop()
        self._cancel = cancel or False
        self._close_default = close_default or True

    def close(self):
        if not self._close_default or self._loop.is_closed():
            return
        if not self._loop.is_running():
            self._loop.close()
            self._loop = None

    def stop(self):
        if self._loop.is_running():
            self._loop.stop()

    def _partital(self, callback, args, keywords):
        return functools.partial(callback, *args, **keywords)

    def call_soon(self, thread_safe=False, callback=None, *args, **keywords):
        args = self._check_args(args)
        partial = self._partital(callback, args, keywords)
        handler = self._loop.call_soon_threadsafe(partial) if thread_safe else self._loop.call_soon(partial)
        self._handler_cancel(handler, self._cancel)
        self._run_forever()
        self.close()

    def call_later(self, delay, callback=None, *args, **keywords):
        args = self._check_args(args)
        partial = self._partital(callback, args, keywords)
        handler = self._loop.call_later(delay, partial)
        self._handler_cancel(handler, self._cancel)
        self._run_forever()
        self.close()

    def call_at(self, when, callback=None, *args, **keywords):
        args = self._check_args(args)
        partial = self._partital(callback, args, keywords)
        handler = self._loop.call_at(when, partial)
        self._handler_cancel(handler, self._cancel)
        self._run_forever()
        self.close()

    def run_until_complete(self, future):
        result = self._loop.run_until_complete(future)
        self.close()
        return result

    def get_loop(self):
        return self._loop

    def time(self):
        return self._loop.time()

    def _check_args(self, args):
        args = args or list()
        args.insert(0, self)
        return args

    def _run_forever(self):
        if not self._loop.is_running():
            self._loop.run_forever()

    def _handler_cancel(self, handler=None, cancel=False):
        if handler and cancel:
            handler.cancel()


def main():
    pass


if __name__ == '__main__':
    main()
