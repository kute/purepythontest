#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test.py
@ __mtime__: 2017/8/3 19:42

"""

import yaml
import re



def main():
    with open("mobiles.yml") as f:
        mobiles = yaml.load(f)
        print(mobiles['HTC'])


if __name__ == "__main__":
    main()
