#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: guess-number.py
@ __mtime__: 2016/8/20 11:15

https://leetcode.com/problems/guess-number-higher-or-lower/

"""

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    if num == 6:
        return 0
    elif num > 6:
        return 1
    else:
        return -1


class Solution(object):

    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        middle = int(n / 2)
        r = guess(middle)
        if r < 0:
            return self.guessNumber(middle + n)
        elif r > 0:
            return self.guessNumber(1 + middle)
        else:
            return middle


def main():
    so = Solution()
    print(so.guessNumber(10))


if __name__ == "__main__":
    main()
