#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/2 21:25'

"""

"""


import tensorflow as tf


def main():
    he = tf.constant('hello, world')
    session = tf.Session()
    session.run(he)


if __name__ == '__main__':
    main()
