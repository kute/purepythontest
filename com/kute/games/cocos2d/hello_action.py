#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/10/30 10:37'

"""

"""

import cocos
from cocos.actions import *


class HelloAction(cocos.layer.ColorLayer):

    def __init__(self):
        super(HelloAction, self).__init__(64, 64, 224, 255)

        self.myscale = ScaleBy(3, duration=2)

        self.label = self.init_label()
        self.add(self.label)

        self.sprite = self.create_sprite()
        # self.add(self.sprite, z=1)

        self.do_action()

    def do_action(self):
        # self.label.do(action=Repeat(self.myscale + Reverse(self.myscale)))
        # self.label.do(action=Repeat(MoveBy((50, 100), duration=2) + Reverse(MoveBy((50, 100), duration=2))))
        # self.label.do(action=Repeat(JumpBy((50, 100), 200, 5, duration=10) + Reverse(JumpBy((50, 100), 200, 5, duration=2))))
        # self.label.do(action=(Delay(4)))
        self.label.do(action=(MoveTo((100,100), 10) | RotateBy(360, 10) * 2))
        # self.label.do(action=(Waves3D(duration=2) + StopGrid()))
        # self.label.do(action=(CallFuncS(lambda label: print(label))))
        # self.label.do(action=Repeat(ToggleVisibility()))
        # self.label.do(action=Repeat(Reverse(self.myscale) + self.myscale))

    def init_label(self):
        label = cocos.text.Label(
            text="Hello world",
            font_name='Times New Roman',
            font_size=32,
            anchor_x="center",
            anchor_y="center",
            position=(320, 240)
        )
        return label

    def create_sprite(self):
        return cocos.sprite.Sprite(image="a.jpg", position=(320, 240), scale=3)


def main():
    cocos.director.director.init()
    cocos.director.director.set_depth_test()
    mainscene = HelloAction()
    # mainscene.do(Repeat(RotateBy(360, duration=10)))
    cocos.director.director.run(cocos.scene.Scene(mainscene))


if __name__ == '__main__':
    main()
