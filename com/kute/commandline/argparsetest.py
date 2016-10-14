#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/5/12 21:13'
# see com.kute.text.encoding_detect.py

import argparse


def main():
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
                        help="the given file dir path, used to detect echo file content encoding under given file dir.",
                        type=str)
    parser.add_argument("--separator",
                        help="the separator between filename and encoding when you use the '-d' or '--dir', default is \
                              '=', such as 'myfilename=utf-8'.",
                        type=str, default="=")
    args = parser.parse_args()
    print(args.file)
    if args.file:
        print( "filename")
    print( args.pretty)
    print( args.ungly)
    print( args.tty)
    print( args.number)


if __name__ == '__main__':
    main()
