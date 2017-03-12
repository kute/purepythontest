#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/12 10:21'

"""

"""

import jieba


def main():
    # jieba.enable_parallel(4)
    text = "我们来到了北京饭店"
    print(" ".join(jieba.cut(text)))
    print(jieba.get_FREQ('北京饭店'), jieba.get_FREQ('北京'), jieba.get_FREQ('饭店'))
    print("=" * 10)
    # 定义词库, 分隔 北京  饭店
    jieba.set_dictionary('my_dict.txt')
    print(" ".join(jieba.cut('今天天气不错')))
    print(jieba.get_FREQ('北京饭店'), jieba.get_FREQ('北京'), jieba.get_FREQ('饭店'))
    print(" ".join(jieba.cut(text)))
    print("=" * 10)
    print(" ".join(jieba.cut('藏宝阁太贵')))
    jieba.suggest_freq(('太', '贵'), True)
    print(" ".join(jieba.cut('藏宝阁太贵')))


if __name__ == '__main__':
    main()
