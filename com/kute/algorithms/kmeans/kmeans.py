#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: kmeans.py
@ __mtime__: 2017/2/21 15:07

kmeans 二维点坐标 计算 图示

测试样本：two_dimension_location.txt

"""

import numpy as np
from math import sqrt, pow
from collections import defaultdict

np.random.seed(2017)


class Kmeans(object):

    def __init__(self, k, filepath, seedloc):
        if not filepath:
            raise ValueError("should special the file path.")
        self.k = k
        self.filepath = filepath
        self.nlocationarray = None

        self._load_txt()
        self.shape = self.nlocationarray.shape
        self.seedlocarray = seedloc or self._gen_seed()

        self.resultmap = defaultdict(list)

        self._start()

    def _gen_seed(self):
        """从样本中随机出k个点
        """
        indexary = np.random.choice(self.shape[0], size=self.k, replace=False)
        return self.nlocationarray[indexary]

    def _load_txt(self):
        with open(self.filepath) as fp:
            self.nlocationarray = np.loadtxt(fp, delimiter=",", dtype=float)
            if len(self.nlocationarray) == 0:
                raise ValueError("there is not enough data in file {}.".format(self.filepath))

    def _euclidean_distance(self, location_x, location_y):
        """欧氏距离
        """
        xlen, ylen = len(location_x), len(location_y)
        if xlen != ylen:
            raise TypeError("tuple {} and {} should be the same-size tuple.".format(location_x, location_y))
        xloc, yloc = location_x, location_y
        xysum = 0
        for i in range(xlen):
            xysum += pow((xloc[i] - yloc[i]), 2)
        # 不作精度要求
        return sqrt(xysum)

    def _is_closure(self, taskresultmap):
        """判断是否结果收敛（最近两次的结果一致）
        """
        if len(self.resultmap) == 0:
            return False
        for key, countrys in self.resultmap.items():
                if len(set(countrys) - set(taskresultmap[key])) > 0:
                    return False
        return True

    def _cal_location(self, datalist):
        datasize = len(datalist)
        size = len(self.datamap[datalist[0]])
        locationlist = []
        for i in range(size):
            total = sum([self.datamap[name][i] for name in datalist])
            locationlist.append(round(total / datasize, 4))
        return tuple(locationlist)

    def _determining_seed(self):
        """选取新的种子点（点左边取均值）
        """
        if len(self.resultmap) > 0:
            self.seedlist.clear()
            for index, countrylist in self.resultmap.items():
                self.seedlist.append(self._cal_location(countrylist))
            self.seedmap = self._return_seed_map()
            return True
        return False

    def _start(self):
        taskresultmap = defaultdict(list)
        for location in self.nlocationarray:
            distancemap = {}
            for index, seedloc in enumerate(self.seedlocarray):
                distancemap[index] = self._euclidean_distance(location, seedloc)
            key_min_distance = min(distancemap, key=distancemap.get)
            taskresultmap[key_min_distance].append(location)
        print(taskresultmap)
        # if not self._is_closure(taskresultmap):
        #     self.resultmap = taskresultmap.copy()
        #     if self._determining_seed():
        #         self._start()

    @property
    def result(self):
        return self.resultmap


def main():
    filepath = "two_dimension_location.txt"
    kmeans = Kmeans(3, filepath, None)
    print(kmeans.result)


if __name__ == "__main__":
    main()
