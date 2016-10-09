#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/24 22:20'

"""

BM 字符串搜索

"""


def search(pattern, text):
    pl = len(pattern)
    tl = len(text)
    if tl < pl:
        return -1
    i = pl - 1
    j = i

    while j < tl:
        while pattern[i] == text[j]:
            if i == 0:
                return j
            if j == tl - 1:
                return -1
            i -= 1
            j -= 1
        index = pattern.rfind(text[j])
        if index == -1:
            j += pl
        else:
            j += pl - index - 1
        i = pl - 1
    return -1


def main():
    text = "HERE IS A SIMPLE AXAMPLE"
    pattern = "I"
    result = search(pattern, text)
    print(result)


if __name__ == '__main__':
    main()
