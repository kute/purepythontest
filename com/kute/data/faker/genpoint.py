#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: genpoint.py
@ __mtime__: 2017/2/24 16:13

n维点坐标 测试数据

"""

import attr
import random
from faker import Factory
import math
import numpy as np
from faker.providers import BaseProvider


class PointProvider(BaseProvider):

    def two_dimension(self, r, nums=2):
        pointlist = []
        for i in range(nums):
            radius = r * random.random()
            ang = random.random() * 2 * math.pi
            pointlist.append([radius * math.cos(ang), radius * math.sin(ang)])
        return np.array(pointlist)


class PointDataGenerator(object):

    def __init__(self, dimension=2, nums=1, r=20):
        self.dimension = dimension
        self.nums = nums
        self.r = r

    @property
    def data(self):
        fake = Factory.create('zh_CN')
        fake.add_provider(PointProvider)
        if self.dimension == 2:
            return fake.two_dimension(self.r, self.nums)
        return None


def main():
    p = PointDataGenerator(2, 10, 20)
    print(p.data)


if __name__ == "__main__":
    main()
