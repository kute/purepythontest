#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/7 21:02'

"""

"""

import cocos
from com.kute.games.cocos2d.examples.make7.constant import constants
from com.kute.games.cocos2d.examples.make7.wk_layer import *


def main():
    cocos.director.director.init(width=constants["container"]["width"], height=constants["container"]["height"])
    cocos.director.director.run(cocos.scene.Scene(BackgroundLayer()))


if __name__ == '__main__':
    main()
