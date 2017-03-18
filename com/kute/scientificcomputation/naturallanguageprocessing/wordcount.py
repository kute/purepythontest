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


class WordCount(object):

    def __init__(self, data=None):
        self.data = data

    def count(self, n=None):
        return Counter(self.data).most_common(n)

    def count_for_en(self):
        return TextBlob(self.data).word_counts

    def count_for_zh(self, n=None):
        self.data = jieba.lcut(self.data)
        return self.count(n)

    def words_for_en(self):
        return TextBlob(self.data).words

    def words_for_zh(self):
        return jieba.lcut(self.data)

    def _count_default_dict(self):
        dd = defaultdict(int)
        for word in self.data:
            dd[word] += 1
        return dd


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
    print(WordCount(s1).count())
    print(WordCount(s1)._count_default_dict())
    print(WordCount(s2).count())
    print(WordCount(s2)._count_default_dict())

    # 分词后统计
    print(WordCount(s1).count_for_en())
    print(WordCount(s2).count_for_zh())


if __name__ == "__main__":
    main()
