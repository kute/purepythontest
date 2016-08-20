#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: longbai 
@ __file__: ransom-note.py
@ __mtime__: 2016/8/20 10:52

"""


class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        for letter in ransomNote:
            if ransomNote.count(letter) > magazine.count(letter):
                return False
        return True


def main():
    so = Solution()
    print(so.canConstruct("aa", "aab"))


if __name__ == "__main__":
    main()
