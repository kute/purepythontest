#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: test2342.py
@ __mtime__: 2016/11/3 18:59

"""


from captcha_solver import CaptchaSolver


def main():
    solver = CaptchaSolver('browser')
    with open('gpin.jpg', 'rb') as inp:
        raw_data = inp.read()
        print(raw_data.decode("utf-8"))
        print(solver.solve_captcha(raw_data))


if __name__ == "__main__":
    main()
