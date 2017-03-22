#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/20 22:04'

"""

"""


from sklearn.feature_extraction.text import TfidfVectorizer


def main():
    vect = TfidfVectorizer(min_df=1)
    tfidf = vect.fit_transform(['我喜欢苹果',
                                '我爱苹果'])
    print((tfidf * tfidf.T).A)


if __name__ == '__main__':
    main()
