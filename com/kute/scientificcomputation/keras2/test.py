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
import keras


def main():
    y_train = (50000, 1)
    y_train = keras.utils.to_categorical(y_train, 10)
    print(y_train)


if __name__ == "__main__":
    main()
