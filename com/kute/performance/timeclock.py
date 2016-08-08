#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/6/15 11:23'


orignal_str = "sdf a sdi sdksdj sd fsjdkfjwejsd sd fsdjkfs fsdk fsdj skdjf sdf sdjf skdjf sdfj sdkfj sdfd sd s s s"


def main():
    _time_analyze_(slow_replace)
    _time_analyze_(slowest_replace)
    _time_analyze_(fast_replace)
    _time_analyze_(fastest_replace)


def slowest_replace():
    replace_list = []
    for i, char in enumerate(orignal_str):
        c = char if char != " " else "-"
        replace_list.append(c)
    return "".join(replace_list)


def slow_replace():
    replace_str = ""
    for i, char in enumerate(orignal_str):
        c = char if char != " " else "-"
        replace_str += c
    return replace_str


def fast_replace():
    return "-".join(orignal_str.split())


def fastest_replace():
    return orignal_str.replace(" ", "-")


def _time_analyze_(func):
    from time import clock
    start = clock()
    for i in range(10000):
        func()
    finish = clock()
    print "{:<20}{:10.6} s".format(func.__name__ + ":", finish - start)


if __name__ == '__main__':
    main()
