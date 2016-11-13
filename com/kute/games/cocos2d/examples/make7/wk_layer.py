#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/7 21:02'

"""

"""

import cocos
from com.kute.games.cocos2d.examples.make7.constant import *
from com.kute.games.cocos2d.examples.make7.storage import PointHexagonStorage
from cocos.layer import ColorLayer, MultiplexLayer
from cocos.tiles import HexMapLayer
from cocos.sprite import Sprite

from math import sqrt


class BackgroundLayer(ColorLayer):

    is_event_handler = True

    def __init__(self):
        super(BackgroundLayer, self).__init__(r=25, g=29, b=45, a=255)

        self.toppanel = self.__init_top_panel()
        self.playpanel = self.__init_play_panel()
        self.switchpanel = self.__init_switch_panel()
        self.toolpanel = self.__init_tool_panel()

        self.add(self.toppanel, z=1)
        self.add(self.playpanel, z=1)
        self.add(self.switchpanel, z=1)
        self.add(self.toolpanel, z=1)

    def __init_top_panel(self):
        height = constants["toolpanel"]["height"]
        toppanel = TopPanelLayer(height, self.width)
        toppanel.position = (0, self.height - height)
        return toppanel

    def __init_play_panel(self):
        height = constants["playpanel"]["height"]
        playpanel = PlayPanelLayer(height, self.width)
        playpanel.position = (0, self.height - height - self.toppanel.height)
        return playpanel

    def __init_switch_panel(self):
        height = constants["switchpanel"]["height"]
        switchpanel = SwitchPanelLayer(height, self.width)
        switchpanel.position = (0, self.height - self.toppanel.height - self.playpanel.height - height)
        return switchpanel

    def __init_tool_panel(self):
        height = constants["toolpanel"]["height"]
        toolpanel = ToolPanelLayer(height, self.width)
        toolpanel.position = (0, self.height - self.toppanel.height - self.playpanel.height - self.switchpanel.height -
                              self.height)
        return toolpanel

    def draw(self):
        # self.add(self.toppanel, z=1)
        # self.add(self.playpanel, z=1)
        # self.add(self.switchpanel, z=1)
        # self.add(self.toolpanel, z=1)
        pass


class TopPanelLayer(ColorLayer):
    def __init__(self, height=80, width=constants["container"]["width"]):
        super(TopPanelLayer, self).__init__(r=255, g=255, b=255, a=255, width=width, height=height)


class PlayPanelLayer(ColorLayer):
    def __init__(self, height=360, width=constants["container"]["width"]):
        super(PlayPanelLayer, self).__init__(r=25, g=29, b=45, a=255, width=width, height=height)

        centersprite = WkSprite(position=(self.width / 2, self.height / 2))
        self.add(centersprite)
        self.six_hexagon_position = list()
        self.create_hexagon(center_sprite=centersprite, level=2)

    def create_hexagon(self, center_sprite=None, level=2):
        """create six hexagon around the center-hexagon
        :param level:
        :param center_sprite:
        """
        if not center_sprite:
            return
        x, y = center_sprite.position
        w = center_sprite.width
        h = center_sprite.height
        temp = sqrt(3) * w / 6
        extra = 4
        self.six_hexagon_position = self.__get_six_hexagon_position(x, y, w, h, temp, extra)
        for position in self.six_hexagon_position:
            print(position)
            sprite = WkSprite(position=position)
            PointHexagonStorage.add(position, sprite)
            self.add(sprite, z=1)
        print(PointHexagonStorage.hexagonmap)

    def __get_six_hexagon_position(self, x, y, w, h, temp, extra=4):
        """the position of six hexagon around the center-hexagon(x, y) is below:
        (x + w / 2, y + h - sqrt(3) * w / 6)
        (x + w, y)
        (x + w / 2, y - h + sqrt(3) * w / 6)
        (x - w / 2, y - h + sqrt(3) * w / 6)
        (x - w, y )
        (x - w / 2, y + h - sqrt(3) * w / 6)
        """
        return [
            (x + w / 2 + extra, y + h - temp + extra),
            (x + w + extra, y),
            (x + w / 2 + extra, y - h + temp - extra),
            (x - w / 2, y - h + temp - extra),
            (x - w - extra, y),
            (x - w / 2, y + h - temp + extra)
        ]


class SwitchPanelLayer(ColorLayer):
    def __init__(self, height=120, width=constants["container"]["width"]):
        super(SwitchPanelLayer, self).__init__(r=255, g=0, b=255, a=255, width=width, height=height)


class ToolPanelLayer(ColorLayer):
    def __init__(self, height=80, width=constants["container"]["width"]):
        super(ToolPanelLayer, self).__init__(r=255, g=255, b=0, a=255, width=width, height=height)


class WkSprite(Sprite):

    def __init__(self, position=None):
        super(WkSprite, self).__init__(sprite_image, position)


def main():
    pass


if __name__ == '__main__':
    main()
