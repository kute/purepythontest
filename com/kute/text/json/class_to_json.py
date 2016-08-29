#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/8/29 21:33'

"""

json与class转换

"""

import json
import datetime
from collections import namedtuple


def main():
    # 1. class to json
    c = Comment("aes258", "my body", 235, 9, datetime.datetime.now().__str__())
    jsonstr = json.dumps(c, default=lambda obj: obj.__dict__)
    print(jsonstr)

    # 2. class to json
    jsonstr = c.to_json()
    print(jsonstr)

    # 3. json to class
    c2 = Comment.from_json(jsonstr)
    print(c2)

    # 4. json to class
    c3 = Comment.from_json_2(jsonstr)
    print(c3.content)


class Comment(object):
    """just comment object"""
    def __init__(self, commentid, content, vote, against, createtime):
        self.commentid = commentid
        self.content = content
        self.vote = vote
        self.against = against
        self.createtime = createtime

    @classmethod
    def from_json(cls, jsonstr):
        jsonobj = json.loads(jsonstr)
        return cls(**jsonobj)

    @classmethod
    def from_json_2(cls, jsonstr):
        return json.loads(jsonstr,
                          object_hook=lambda j: namedtuple(cls.__name__, j.keys())(*j.values()))

    def to_json(self):
        return json.dumps({
            "commentid": self.commentid,
            "content": self.content,
            "vote": self.vote,
            "against": self.against,
            "createtime": self.createtime
        })

    def __str__(self):
        return " ".join([self.__class__.__name__, "[", ", ".join([self.commentid, self.content, str(self.vote),
                                                                  str(self.against), self.createtime]), "]"])


if __name__ == '__main__':
    main()
