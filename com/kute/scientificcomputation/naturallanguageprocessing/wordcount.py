#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: wordcount.py
@ __mtime__: 2017/3/17 16:03

词频统计

"""

from collections import Counter, defaultdict
import jieba
from textblob import TextBlob


def main():
    s1 = 'No matter how you count the words, you can only write to the file once all words are counted; otherwise ' \
         'you are writing once for each "count", and as soon as the word appears more than once, you will have ' \
         'doubled out your output'
    s2 = '结果奇异向量以及奇异值矩阵用于将文档向量和查询向量映射到一个子空间中，在该空间中，来自文档矩阵的语义关系被保' \
         '留。最后，可以通过标准化的内积计算来计算向量之间的夹角余弦相似度，进而根据计算结果比较文本间的相似度。' \
         'LSI引入的唯一变化就是剔除小的奇异值，因为与小的奇异值相关联的特征实际上在计算相似度时并不相关，将它们包括进来' \
         '将降低相关性判断的精确度。保留下来的特征是那些对文档向量在m维空间中的位置大有影响的特征。剔除小的奇异值将文档特' \
         '征空间变为文档概念空间。概念向量之问使用内积的夹角余弦相似度计算比原来基于原文本向量的相似度计算更可靠'

    # 未分词直接统计单个单词的频率
    print(Counter(s1).most_common())
    print(Counter(s2).most_common())
    print(test1(s1))
    print(test1(s2))

    # 分词后统计
    print(TextBlob(s1).word_counts)
    print(Counter(jieba.lcut(s2)).most_common())


def test1(s):
    dd = defaultdict(int)
    for word in s:
        dd[word] += 1
    return dd


if __name__ == "__main__":
    main()
