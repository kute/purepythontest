#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: TF-IDF.py
@ __mtime__: 2017/3/17 15:46

http://www.cnblogs.com/biyeymyhjob/archive/2012/07/17/2595249.html

TF-IDF（term frequency–inverse document frequency  词频-逆向文档频率） 算法：

统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降

"""

from collections import Counter


def main():
    s1 = 'hello'
    s2 = '统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度'
    print(Counter(s2).most_common())


if __name__ == "__main__":
    main()
