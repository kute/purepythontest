#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: constant.py
@ __mtime__: 2016/11/8 13:07

"""

class Constant(object):
    container_width = 480
    container_height = 640

    top_panel_height = 80
    play_panel_height = 360
    switch_panel_height = 120
    tool_panel_height = 80

constants = {
    "container": {
        "width": 480,
        "height": 640
    },
    "toppanel": {
        "height": 80
    },
    "playpanel": {
        "height": 360
    },
    "switchpanel": {
        "height": 120
    },
    "toolpanel": {
        "height": 80
    }
}


def main():
    print("hello")


if __name__ == "__main__":
    main()
