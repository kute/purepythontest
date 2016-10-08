#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: loadfromfile.py
@ __mtime__: 2016/9/23 18:14

"""

import numpy as np


def main():
    try:
        with open("data.txt", "r") as fp:
            arry = np.loadtxt(fname=fp, delimiter=", ", dtype="<U1")
            print(arry.ndim)
            print(arry.shape)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
