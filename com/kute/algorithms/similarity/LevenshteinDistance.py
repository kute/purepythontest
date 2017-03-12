#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/5/24 21:40'

"""

字符串编辑距离: 由一个转换为另一个所需要的最少编辑次数

"""


def main():
    s = "GUMBO"
    t = "GAMBOL"
    n = len(s)  # 5
    m = len(t)  # 6
    martix = [range(n + 1) for x in range(m + 1)]

    for i in range(n+1):
        martix[0][i] = i
    for j in range(m+1):
        martix[j][0] = j
    for j in range(1, m+1):
        for i in range(1, n+1):
            if t[j-1] == s[i-1]:
                martix[j][i] = min(martix[j][i-1] + 1, martix[j-1][i] + 1, martix[j-1][i-1])
            else:
                martix[j][i] = min(martix[j][i-1] + 1, martix[j-1][i] + 1, martix[j-1][i-1] + 1)
    print(martix[m][n])


if __name__ == '__main__':
    main()
