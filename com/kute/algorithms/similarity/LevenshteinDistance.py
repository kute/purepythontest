#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/5/24 21:40'

"""

字符串编辑距离: 由一个转换为另一个所需要的最少编辑次数

自己是实现

"""

import Levenshtein
import numpy as np
import copy


def levenshtein_distance(len1, len2, s1, s2):
    """动态规划（递归）
    设  distance(i, j) 代表 i个长度的字串A 与 j个长度的字串B 的编辑距离，有如下公式：
    if i == 0 and j > 0 then distance(i, j) = j
    if j == 0 and i > 0 then distance(i, j) = i
    if i == 0 and j == 0 then distance(i, j) = 0
    if i > 0 and j > 0 then distance(i, j) = min(distance(i - 1, j) + 1, distance(i, j - 1) + 1, distance(i - 1, j - 1) + f(i, j)) 其中，若
    A第i个元素等于B第j个元素， 则 f(i, j) = 0, 否则 f(i, j) = 1
    非最优，且存在stackoverflow
    :param len1: len(s1)
    :param len2: len(s2)
    :param s1
    :param s2
    """
    if len1 == 0 or len2 == 0:
        return len1 + len2
    subdis = 0 if s1[len1 - 1] == s2[len2 - 1] else 1
    return min(levenshtein_distance(len1 - 1, len2, s1, s2) + 1,
               levenshtein_distance(len1, len2 - 1, s1, s2) + 1,
               levenshtein_distance(len1 - 1, len2 - 1, s1, s2) + subdis)


def levenshtein_ld(s1, s2):
    """
    矩阵迭代 存储编辑距离
    当前 = min(左，上，左上)
    """
    len1, len2 = len(s1), len(s2)
    ld = np.matrix(np.zeros((len1 + 1, len2 + 1), dtype=int))
    for i in range(1, len2 + 1):
        ld[0, i] = i
    for j in range(1, len1 + 1):
        ld[j, 0] = j
    for i in range(1, len1 + 1):
        for j in range(1, len2 + 1):
            subdis = 0 if s1[i - 1] == s2[j - 1] else 1
            ld[i, j] = min(ld[i - 1, j] + 1,
                           ld[i, j - 1] + 1,
                           ld[i - 1, j - 1] + subdis)
    return ld[len1, len2]


def levenshtein_two_row(s1, s2):
    """
    用两个向量，保存当前编辑距离和上一行编辑距离
    """
    len1, len2 = len(s1), len(s2)
    if s1 == s2:
        return 0
    if len1 == 0 or len2 == 0:
        return len1 + len2
    v0 = np.array([i for i in range(len2 + 1)])
    v1 = copy.deepcopy(v0)
    for i in range(len1):
        v1[0] = i + 1
        for j in range(len2):
            subdis = 0 if s1[i] == s2[j] else 1
            v1[j + 1] = min(
                v1[j] + 1,
                v0[j + 1] + 1,
                v0[j] + subdis
            )
        v0[:] = v1[:]
    return v1[len2]


def main():
    # s1, s2 = 'asdf23rsdddfffffffff23rsdfqdfq4', '234rasdfcq23rsdfasdf23'
    s1, s2 = 'werf', 'rwef4'
    len1, len2 = len(s1), len(s2)
    r = levenshtein_distance(len1, len2, s1, s2)
    print(r, Levenshtein.distance(s1, s2))
    r2 = levenshtein_ld(s1, s2)
    print(r2, Levenshtein.distance(s1, s2))
    r3 = levenshtein_two_row(s1, s2)
    print(r3, Levenshtein.distance(s1, s2))


if __name__ == '__main__':
    main()
