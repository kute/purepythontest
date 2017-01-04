#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/10/31 22:11'

"""

"""


import cocos
import pyglet
from cocos.layer import Layer
from cocos.sprite import Sprite


class BackGroundLayer(Layer):
    def __init__(self):
        super(BackGroundLayer, self).__init__()

        self.bg_image = pyglet.resource.image(name="resources/desktop.png")
        # sprite = Sprite(
        #     image=self.bg_image,
        #     scale=1,
        #     position=(320, 240)
        # )
        # self.add(sprite)

    def draw(self, *args, **kwargs):
        self.bg_image.blit(0, 0)


def main():
    pass


if __name__ == '__main__':
    main()
