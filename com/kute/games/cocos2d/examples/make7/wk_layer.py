#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2016/11/7 21:02'

"""

"""

import cocos
from cocos.layer import ColorLayer, MultiplexLayer
from cocos.tiles import HexMapLayer


class Constant(object):
    container_width = 480
    container_height = 640

    top_panel_height = 80
    play_panel_height = 360
    switch_panel_height = 120
    tool_panel_height = 80


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
        height = Constant.tool_panel_height
        toppanel = TopPanelLayer(height, self.width)
        toppanel.position = (0, self.height - height)
        return toppanel

    def __init_play_panel(self):
        height = Constant.play_panel_height
        playpanel = PlayPanelLayer(height, self.width)
        playpanel.position = (0, self.height - height - self.toppanel.height)
        return playpanel

    def __init_switch_panel(self):
        height = Constant.switch_panel_height
        switchpanel = SwitchPanelLayer(height, self.width)
        switchpanel.position = (0, self.height - self.toppanel.height - self.playpanel.height - height)
        return switchpanel

    def __init_tool_panel(self):
        height = Constant.tool_panel_height
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
    def __init__(self, height=80, width=Constant.container_width):
        super(TopPanelLayer, self).__init__(r=255, g=255, b=255, a=255, width=width, height=height)


class PlayPanelLayer(ColorLayer):
    def __init__(self, height=360, width=Constant.container_width):
        super(PlayPanelLayer, self).__init__(r=0, g=255, b=255, a=255, width=width, height=height)


class SwitchPanelLayer(ColorLayer):
    def __init__(self, height=120, width=Constant.container_width):
        super(SwitchPanelLayer, self).__init__(r=255, g=0, b=255, a=255, width=width, height=height)


class ToolPanelLayer(ColorLayer):
    def __init__(self, height=80, width=Constant.container_width):
        super(ToolPanelLayer, self).__init__(r=255, g=255, b=0, a=255, width=width, height=height)



def main():
    pass


if __name__ == '__main__':
    main()
