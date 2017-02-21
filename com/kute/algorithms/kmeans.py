#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: kmeans.py
@ __mtime__: 2017/2/20 14:41

http://www.csdn.net/article/2012-07-03/2807073-k-means

数据摘自下文的规格化后的数据
http://www.cnblogs.com/leoo2sk/archive/2010/09/20/k-means.html

"""

from collections import defaultdict, OrderedDict
from math import sqrt


class KMeans(object):
    def __init__(self, k, datamap, seedname, seedlist):
        self.k = k
        self.datamap = datamap
        self.seedname = seedname
        self.seedlist = seedlist

        self.datalist = list(datamap.values())
        self.seedmap = self._return_seed_map()

        self.resultmap = defaultdict(list)

        self.retry = 0
        self.maxretry = 100

    def _return_seed_map(self):
        return OrderedDict(zip(self.seedname, self.seedlist))

    def euclidean_distance(self, location_x, location_y):
        """欧氏距离
        """
        xlen, ylen = len(location_x), len(location_y)
        if not isinstance(location_x, tuple) or not isinstance(location_y, tuple) or xlen != ylen:
            raise TypeError("tuple {} and {} should be the same-size tuple.".format(location_x, location_y))
        xloc, yloc = location_x, location_y
        xysum = 0
        for i in range(xlen):
            xysum += pow((xloc[i] - yloc[i]), 2)
        return sqrt(xysum)

    def _is_closure(self, tempresult):
        """判断是否结果收敛（最近两次的结果一致）
        """
        if len(self.resultmap) == 0:
            return False
        for key, countrys in self.resultmap.items():
                if len(set(countrys) - set(tempresult[key])) > 0:
                    return False
        return True

    def _determining_seed(self):
        """选取新的种子点（点左边取均值）
        """
        if len(self.resultmap) > 0:
            self.seedlist.clear()
            for index, countrylist in self.resultmap.items():
                self.seedlist.append(self._cal_location(countrylist))
            self.seedmap = self._return_seed_map()
            # print(self.seedmap)

    def _cal_location(self, datalist):
        datasize = len(datalist)
        size = len(self.datamap[datalist[0]])
        locationlist = []
        for i in range(size):
            total = sum([self.datamap[name][i] for name in datalist])
            locationlist.append(round(total / datasize, 4))
        return tuple(locationlist)

    def start(self):
        self.retry += 1
        print("========this is {} begin and result=======".format(self.retry))
        tempresult = defaultdict(list)
        for countryname, location in self.datamap.items():
            temp = {}
            for index, seedloc in self.seedmap.items():
                temp[index] = self.euclidean_distance(location, seedloc)
                # print(index, seedloc)
            key = min(temp, key=temp.get)
            # print(countryname, location, key, temp)
            tempresult[key].append(countryname)
        print(tempresult)
        # print(self.seedmap, tempresult, self.resultmap)
        if not self._is_closure(tempresult) and self.retry <= self.maxretry:
            self.resultmap = tempresult.copy()
            self._determining_seed()
            self.start()


def main():
    datamap = {
        "zhongguo": (1, 1, 0.5),
        "riben": (0.3, 0, 0.19),
        "hanguo": (0, 0.15, 0.13),
        "yilang": (0.24, 0.76, 0.25),
        "shate": (0.3, 0.76, 0.06),
        "yilake": (1, 1, 0),
        "kataer": (1, 0.76, 0.5),
        "alianqiu": (1, 0.76, 0.5),
        "wuzibiekesitan": (0.7, 0.76, 0.25),
        "taiguo": (1, 1, 0.5),
        "yuenan": (1, 1, 0.25),
        "aman": (1, 1, 0.5),
        "balin": (0.7, 0.76, 0.5),
        "chaoxian": (0.7, 0.68, 1),
        "yinni": (1, 1, 0.5)
    }

    country_name = ["riben", "balin", "taiguo"]
    seedlist = [datamap[seed] for seed in country_name]
    k = 3
    seed_name = list(range(k))
    kmeans = KMeans(k, datamap, seed_name, seedlist)
    kmeans.start()
    print("======final result========")
    print(kmeans.resultmap)

if __name__ == "__main__":
    main()
