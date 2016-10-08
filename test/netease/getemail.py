#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: getemail.py
@ __mtime__: 2016/9/22 15:51

"""


def main():
    try:
        fileprefix = "550error-{}.txt"
        tofileprefix = "550erroremail-{}.txt"
        for i in range(1, 9):
            file = fileprefix.format(i)
            tofile = tofileprefix.format(i)
            print("........deal with {}".format(file))
            with open(tofile, "a") as f:
                with open(file, "r") as fp:
                    for line in fp:
                        index = line.rfind(": ")
                        if index != -1:
                            email = line[index + 2:].strip()
                            f.write(email + "\n")
            print("......done with {}".format(tofile))

    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
