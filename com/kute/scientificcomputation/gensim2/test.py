#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/21 12:37'

"""

"""

from pprint import pprint
from collections import Counter
from gensim import corpora


def main():
    documents = ["Human machine interface for lab abc computer applications",
                 "A survey of user opinion of computer system response time",
                 "The EPS user interface management system",
                 "System and human system engineering testing of EPS",
                 "Relation of user perceived response time to error measurement",
                 "The generation of random binary unordered trees",
                 "The intersection graph of paths in trees",
                 "Graph minors IV Widths of trees and well quasi ordering",
                 "Graph minors A survey"]
    stoplist = set('for a of the and to in'.split())
    # 过滤 stop word
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]

    # 统计 word count 并过滤 count <= 1
    c = Counter()
    for text in texts:
        c.update(Counter(text))
    texts = [[token for token in text if c[token] > 1] for text in texts]
    pprint(texts)

    # 构建词典
    dictionary = corpora.Dictionary(texts)
    dictionary.save('dictionary.dict')
    print(dictionary)
    print(dictionary.token2id)  # 单词以及在词典中的编号(id)
    # 将指定的document通过字典转换为 document中的每个词在词典中的编号以及出现的次数: (编号, 次数)
    test_document = 'user computer haha eps human human'
    print(dictionary.doc2bow(test_document.lower().split()))

    # 计算texts
    corpus = [dictionary.doc2bow(text) for text in texts]
    corpora.MmCorpus.serialize('deerwester.mm', corpus)  # store to disk
    pprint(corpus)


if __name__ == '__main__':
    main()
