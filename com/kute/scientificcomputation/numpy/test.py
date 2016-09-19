#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/19 21:57'

"""

"""

import numpy as np
from kute.easylog.easylog import geteasylog


easylog = geteasylog()


def main():
    data1 = [1, 9.3, 23, 3, 23.13]
    ary1 = np.array(data1)
    easylog.info(ary1.shape)

    data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
    ary2 = np.array(data2)
    easylog.info(ary2.shape)   # shape 几维数组
    easylog.info(ary2.dtype)   # 数据类型


if __name__ == '__main__':
    main()
