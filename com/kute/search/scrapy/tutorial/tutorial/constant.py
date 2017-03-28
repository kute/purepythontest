#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/27 22:25'

"""

"""


unit_dict = {
    "k": 1000,
    "K": 1000,
    "w": 10000,
    "W": 10000
}


def to_number(origin, loader_context):
    """
    1.9k to 1900
    """
    if any(map(lambda e: e in origin, ['k', 'K', 'w', 'W'])):
        length = len(origin)
        return int(float(origin[0: length - 1]) * unit_dict[origin[length - 1:]])
    else:
        return origin


def add_unit(value, loader_context):
    """
    loader_context 可以传递修改额外的参数, 默认值
    """
    unit = loader_context.get('extra_unit_param', 'default_value')
    return value + unit


def main():
    pass


if __name__ == '__main__':
    main()
