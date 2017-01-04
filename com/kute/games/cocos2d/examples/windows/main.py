#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/10/31 22:05'

"""

windows desktop

"""

import cocos
from cocos.actions import *
from cocos.director import director
from cocos.scene import Scene
from cocos.layer import Layer
from com.kute.games.cocos2d.examples.windows.wk_layers import BackGroundLayer


def main():
    director.init(width=900, height=498)
    director.set_depth_test()

    desktopScene = Scene(BackGroundLayer())
    director.run(desktopScene)


if __name__ == '__main__':
    main()
