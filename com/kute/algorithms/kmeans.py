#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: kmeans.py
@ __mtime__: 2017/2/20 14:41

http://www.csdn.net/article/2012-07-03/2807073-k-means
http://www.cnblogs.com/leoo2sk/archive/2010/09/20/k-means.html


"""

from collections import defaultdict
from math import sqrt


class KMeans(object):
    def __init__(self, k, datamap, seedlist):
        self.k = k
        self.datamap = datamap
        self.seedlist = seedlist

        self.puredatamap = {name: location for name, location in self.datamap.items() if location not in self.seedlist}
        self.datalist = list(datamap.values())
        self.puredatalist = list(filter(lambda x: x not in self.seedlist, self.datalist))
        self.seedmap = {i: location for i, location in enumerate(self.seedlist)}

        self.resultmap = defaultdict(list)

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
        pass

    def start(self):
        tempresult = defaultdict(list)
        for countryname, location in self.puredatamap.items():
            temp = {}
            for nth, seedloc in self.seedmap.items():
                temp[nth] = self.euclidean_distance(location, seedloc)
            key = min(temp, key=temp.get)
            tempresult[key].append(countryname)
            if tempresult[key] in self.datalist:
                name = list(self.datamap.keys())[self.datalist.index(tempresult[key])]
                print(name)

        self.resultmap = tempresult.copy()
        # if not self._is_closure(tempresult):
        #     self._determining_seed()
            # self.start()


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

    seed_name = ["riben", "balin", "taiguo"]
    seedlist = [datamap[seed] for seed in seed_name]
    kmeans = KMeans(3, datamap, seedlist)
    kmeans.start()
    print(kmeans.resultmap)
    resultmap = defaultdict(list)
    print(len(resultmap))


if __name__ == "__main__":
    main()
