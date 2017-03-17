#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/12 15:11'

"""

"""

from textblob import TextBlob


def main():
    text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''
    blob = TextBlob(text)
    print(blob.tags)
    print(blob.noun_phrases)
    print(blob.words)
    print(blob.word_counts)
    print(blob.sentences)
    print(blob.sentiment)


if __name__ == '__main__':
    main()
