#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test.py
@ __mtime__: 2017/7/27 20:14

"""

from keras.models import Sequential
from keras.layers import Dense, Activation


def main():
    model = Sequential()
    model.add(Dense(units=32, input_shape=(784, )))
    model.add(Activation(10))

    model.compile()


if __name__ == "__main__":
    main()
