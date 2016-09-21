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
    easylog.info(ary2.ndim)
    easylog.info(ary2.shape)   # shape 几维数组
    easylog.info(ary2.dtype)   # 数据类型

    easylog.info(np.zeros((3, 5)))
    easylog.info(np.zeros_like(ary2))

    easylog.info(np.ones((3, 5)))

    easylog.info(np.empty((3, 5)))  # random
    easylog.info(np.random.random((3, 5)))

    easylog.info(np.arange(1, 11).reshape((5, 2)))  # reshape 不改变数组本身,resize 则改变数组本身
    easylog.info(np.arange(1, 11).resize((5, 2)))

    a = np.array([[1, 0], [3, 2]])
    b = np.arange(0, 4).reshape((2, 2))
    a * b  # 只按元素 相乘
    np.dot(a, b)  # 这才是 矩阵乘法

    easylog.info(np.linspace(1, 10, 3, True, True))  # 平均分成 num份, 相同的间隔(space)

    a = np.arange(12).reshape(3, 4)  # 这是 3 x 4  的二维,所以 axis(轴) = 2
    a.sum()  #
    a.sum(axis=0)  # 将求和运算 运用在轴 0上, 也就是 把三行变成 一行, 也就是 按 列 相加
    a.max()
    a.min()

    a = np.fromfunction(lambda x, y: 10 * x + y, (5, 4), dtype=int)
    print(a)
    a[2, 3]  # 一维 可以切片, 索引, 多维 数组可以每个轴有一个索引。这些索引由一个逗号分割的元组给出
    a[1, 1: 3]  # [11, 12]
    a[0: 5, 1]  # [1, 11, 21, 31, 41]
    a[0: 5, 1: 3]  # [[1, 2], [11, 12], [21, 22], [31, 32], [41, 42]]
    a[-1]  # [40, 41, 42, 43]

    a.ravel()  # 展平

    for row in a:
        print(row)

    for element in a.flat:  # flat 是迭代器
        print(element)

    # 组合
    a = np.arange(0, 4).reshape((2, 2))
    b = np.arange(4, 8).reshape((2, 2))
    easylog.info(np.vstack((a, b)))  # 垂直组合,增加 行
    easylog.info(np.hstack((a, b)))  # 水平组合, 增加列


if __name__ == '__main__':
    main()
