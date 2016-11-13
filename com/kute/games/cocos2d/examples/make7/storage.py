#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/13 14:20'

"""

"""

from cocos.sprite import Sprite


class PointHexagonStorage(object):

    hexagonmap = {}

    def __init__(self):
        print("Do nothing")

    @staticmethod
    def __check_position(position=None):
        if not position:
            raise ValueError("Illegal position")
        try:
            tuple(position)
        except Exception as e:
            raise TypeError("position is not the instance of tuple")

    @staticmethod
    def __check_sprite(sprite=None):
        if not sprite:
            raise ValueError("Illegal sprite")

    @staticmethod
    def __key(position=None):
        PointHexagonStorage.__check_position(position)
        return "point_{}_{}_hexagon".format(position[0], position[1])

    @staticmethod
    def add(position=None, sprite=None):
        key = PointHexagonStorage.__key(position)
        PointHexagonStorage.__check_sprite(sprite)
        if not PointHexagonStorage.isexist(position):
            PointHexagonStorage.hexagonmap[key] = sprite

    @staticmethod
    def isexist(position=None):
        key = PointHexagonStorage.__key(position)
        return key in PointHexagonStorage.hexagonmap


def main():
    pass


if __name__ == '__main__':
    main()
