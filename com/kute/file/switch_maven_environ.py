#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: switch_maven_environ.py
@ __mtime__: 2016/10/12 15:22

切换 maven环境（配置文件）

stupid 文件拷贝

"""

import os
import shutil


def main():
    basepath = "D:\\softers\\apache-maven-3.2.5\\conf"
    confdir = [os.path.join(basepath, x) for x in os.listdir(basepath) if os.path.isdir(os.path.join(basepath, x)) and
               x != 'logging']
    confdict = {}
    for k, v in enumerate(confdir):
        print(k, ":", v)
        confdict[k] = v
    numlist = list(range(0, len(confdict), 1))
    choise = int(input("Please select one: "))
    if choise in confdict:
        desfile = os.path.join(basepath, "settings.xml")
        os.remove(desfile)
        shutil.copy(os.path.join(confdict[choise], "settings.xml"), desfile)
        print("Maven environ changed!")
    else:
        print("Wrong input, should be:{}".format(numlist))


if __name__ == "__main__":
    main()
