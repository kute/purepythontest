#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: try_exception_else_finaly.py
@ __mtime__: 2016/12/9 17:57

"""

import sys


def main():
    try:
        raise ValueError("sss")
    except ValueError:
        _, err, _ = sys.exc_info()
        print(err)
    except (FileExistsError, IndexError) as e:
        print(e)
    else:
        print("exec ok")
    finally:
        print("over")


if __name__ == "__main__":
    main()
