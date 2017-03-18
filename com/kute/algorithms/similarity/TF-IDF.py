#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: TF-IDF.py
@ __mtime__: 2017/3/17 15:46

http://www.cnblogs.com/biyeymyhjob/archive/2012/07/17/2595249.html

TF-IDF（term frequency–inverse document frequency  词频-逆向文档频率） 算法：

TF-IDF = TF * IDF

统计方法，用以评估一字词对于一个文件集或一个语料库中的其中一份文件的重要程度。
字词的重要性随着它在文件中出现的次数成正比增加，但同时会随着它在语料库中出现的频率成反比下降

如果某个词或短语在一篇文章中出现的频率TF高，并且在其他文章中很少出现，则认为此词或者短语具有很好的类别区分能力，适合用来分类


词频统计见: com/kute/scientificcomputation/naturallanguageprocessing/wordcount.py

"""
import os
basepath = os.path.dirname(__file__)
import codecs
import math
import numpy as np
from com.kute.scientificcomputation.naturallanguageprocessing.wordcount import WordCount


def main():
    # 这里从简书随便找了几篇关于"人工智能"的文章, 只是用来练习, 没侵权吧
    # source.txt 为目标文章, source{1-5}.txt为语料库
    file = os.path.join(basepath, 'data/source{}.txt')
    keyword = '孵化'
    totalfilecount = 5
    stopwords = ['的', '了', '是', ' ', '却是', '的确']
    with codecs.open(file.format('', 'r', 'utf-8')) as rf, codecs.open(file.format(1), 'r', 'utf-8') as rf1, \
            codecs.open(file.format(2, 'r', 'utf-8')) as rf2, codecs.open(file.format(3, 'r', 'utf-8')) as rf3, \
            codecs.open(file.format(4, 'r', 'utf-8')) as rf4, codecs.open(file.format(5, 'r', 'utf-8')) as rf5:
        content = rf.read()
        kwmap = dict(WordCount(content).count_for_zh())
        # 过滤stopword
        # sumwordcount = sum([kwmap[word] for word in list(set(kwmap.keys()) - set(stopwords))])
        sumwordcount = sum(kwmap.values()) - sum([kwmap[word] for word in stopwords])
        print(sumwordcount, sum(kwmap.values()))
        tf = kwmap[keyword] / sumwordcount

        content1 = rf1.read()
        content2 = rf2.read()
        content3 = rf3.read()
        content4 = rf4.read()
        content5 = rf5.read()
        existcount = int(keyword in WordCount(content1).words_for_zh()) + \
                     int(keyword in WordCount(content2).words_for_zh()) + \
                     int(keyword in WordCount(content3).words_for_zh()) + \
                     int(keyword in WordCount(content4).words_for_zh()) + \
                     int(keyword in WordCount(content5).words_for_zh())
        # idf = math.log(totalfilecount / existcount)
        idf = math.log(totalfilecount / (1 + existcount))
        print('tf={}, totalfilecount={}, existcount={}'.format(tf, totalfilecount, existcount))
        print('keyword: [{}] 的TF-IDF权重为:[{}]'.format(keyword, tf * idf))

        # contentlist = ''.join([content1, content2, content3, content4, content5])
        # wc = WordCount(contentlist)
        # print(wc.count_for_zh(10))


if __name__ == "__main__":
    """
    测试内容源自:
    http://www.jianshu.com/p/bbaafa48fbdd
    http://www.jianshu.com/p/5c78229a6f32
    http://www.jianshu.com/p/9d20e2022a9e
    http://www.jianshu.com/p/c4a3e29d9430
    http://www.jianshu.com/p/fd9be2175809

    """
    main()
