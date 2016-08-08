#! /usr/bin/env python
# -*- coding: utf-8 -*-

import functools

__author__ = 'kute'
# __mtime__ = '16/5/17 21:42'

# http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014318435599930270c0381a3b44db991cd6d858064ac0000


def log(func):
    print 'call %s' % func.__name__

    @functools.wraps(func)
    def wraper():
        print 'sdf'
        return func()
    return wraper


@log
def main():
    print '==='
    return 'ss'


if __name__ == '__main__':
    print main()
