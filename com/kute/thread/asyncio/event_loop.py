#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/8/20 10:28'

"""

"""

import asyncio
import functools


class EventorLoop(object):

    def __init__(self, loop = None):
        if not loop:
            loop = asyncio.get_event_loop()
        self._loop = loop

    def _close(self):
        if self._loop.is_closed():
            return
        self._loop.close()
        self._loop = None

    def _stop(self):
        if self._loop.is_running():
            self._loop.stop()

    def _partital(self, callback, args, keywords):
        return functools.partial(callback, *args, **keywords)

    def call_soon(self, thread_safe=False, cancel=False, callback=None, *args, **keywords):
        args = self._check_args(args)
        partial = self._partital(callback, args, keywords)
        handler = self._loop.call_soon_threadsafe(partial) if thread_safe else self._loop.call_soon(partial)
        self._handler_cancel(handler, cancel)
        self._loop.run_forever()
        self._close()

    def call_later(self, delay, cancel=False, callback=None, *args, **keywords):
        args = self._check_args(args)
        partial = self._partital(callback, args, keywords)
        handler = self._loop.call_later(delay, partial)
        self._handler_cancel(handler, cancel)
        self._loop.run_forever()
        self._close()

    def call_at(self, when, cancel=False, callback=None, *args, **keywords):
        args = self._check_args(args)
        partial = self._partital(callback, args, keywords)
        handler = self._loop.call_at(when, partial)
        self._handler_cancel(handler, cancel)
        self._loop.run_forever()
        self._close()

    def time(self):
        return self._loop.time()

    def _check_args(self, args):
        args = args or list()
        args.insert(0, self._loop)
        return args

    def _handler_cancel(self, handler=None, cancel=False):
        if handler and cancel:
            handler.cancel()


def main():
    pass


if __name__ == '__main__':
    main()
