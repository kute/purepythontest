#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/5/11 22:42'
# 文件以及文本编码检测

import chardet
import urllib
import glob
import argparse
from chardet.universaldetector import UniversalDetector


# 简单文本编码检测
def detectsimplettext(text):
    return 'the encoding of ({}) is {}'.format(text, chardet.detect(text).get('encoding'))


# 检测大文本内容
def detectweburl(url):
    universal = UniversalDetector()
    usock = urllib.urlopen(url)
    for line in usock.readlines():
        universal.feed(line)
        if universal.done:
            break
    universal.close()
    usock.close()
    print('the encoding of ({}) is {}'.format(url, universal.result.get('encoding')))


# 检测文件编码
def detectfile(filepath):
    detector = UniversalDetector()
    for line in open(filepath, 'rb'):
        detector.feed(line)
        if detector.done:
            break
    print('the encoding of ({}) is {}'.format(filepath, detector.result.get('encoding')))


# 检测多个文件的内容编码
def detectfiledir(filedir, separator):
    detector = UniversalDetector()
    for filename in glob.glob(filedir):
        print(filename + "=",)
        detector.reset()
        for line in open(filename, 'rb'):
            detector.feed(line)
            if detector.done:
                break
        detector.close()
        print(detector.result.get('encoding'))


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="this file is used to detect encoding include simple-text, a-web-url, \
                                                 a-file, files-under-filedir.")

    parser.add_argument("-t", "--text",
                        help="the given small text, used to detect the text encoding. suggest to save a file with text \
                             if text is larger.",
                        type=str)
    parser.add_argument("--url", help="the given url, used to detect the web page encoding.", type=str)
    parser.add_argument("-f", "--file",
                        help="the given file path(include filename), used to detect the file content encoding.",
                        type=str)
    parser.add_argument("-d", "--dir",
                        help="the given file dir path, used to detect echo file content encoding under given file dir. \
                             such as /home/app/*.py .",
                        type=str)
    parser.add_argument("--separator",
                        help="the separator between filename and encoding when you use the '-d' or '--dir', default is \
                              '=', such as 'myfilename=utf-8'.",
                        type=str, default="=")
    args = parser.parse_args()
    if args.text:
        detectsimplettext(args.text)
    if args.url:
        detectweburl(args.url)
    if args.file:
        detectfile(args.file)
    if args.dir:
        detectfiledir(args.dir, args.separator)
