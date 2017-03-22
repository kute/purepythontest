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
    texts = [[word for word in document.lower().split() if word not in stoplist] for document in documents]
    # pprint(texts)
    c = Counter()
    for text in texts:
        c.update(Counter(text))
    # print(c.keys())
    texts = [[token for token in text if c[token] > 1] for text in texts]
    pprint(texts)
    dictionary = corpora.Dictionary(texts)
    dictionary.save('dictionary.dict')
    print(dictionary)


if __name__ == '__main__':
    main()
