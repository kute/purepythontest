#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: decision_tree.py
@ __mtime__: 2017/2/14 17:08

分类算法：决策树

相关概念：http://www.cnblogs.com/leoo2sk/archive/2010/09/19/decision-tree.html
信息增益：http://blog.csdn.net/wermnb/article/details/7031246
http://www.cnblogs.com/fantasy01/p/4581803.html
http://blog.csdn.net/alvine008/article/details/37760639

"""

import matplotlib.pyplot as plt
import numpy as np
import math


def main():
    xaxis = [5, 9]
    total = sum(xaxis)
    hs = 0.0
    for x in xaxis:
        px = float(x) / total
        hs -= math.log2(px) * px
    print(hs)


if __name__ == "__main__":
    main()
