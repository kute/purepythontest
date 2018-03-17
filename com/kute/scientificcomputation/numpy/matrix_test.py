#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/7/22 09:43'

"""

矩阵
"""

import numpy as np


def main():
    a = [[1, 1], [1, 0]]
    b = [[1, 1], [1, 0]]

    # 乘积
    result = np.dot(a, b)
    print(result)


if __name__ == '__main__':
    main()
