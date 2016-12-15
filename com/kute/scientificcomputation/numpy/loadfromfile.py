#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: loadfromfile.py
@ __mtime__: 2016/9/23 18:14

"""

import numpy as np
import re

def main():
    try:
        with open("load.txt", "r") as fp:
            arry = np.loadtxt(fname=fp, delimiter="\s+", dtype=str)
            print(arry.ndim)
            print(arry.shape)
            print(arry)
            b = "asdf"
            print(b)
            a = "b'10/31/2016'"
            print(re.sub("b|'", '', a))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
