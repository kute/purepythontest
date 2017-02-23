#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/2/22 21:39'

"""

k-means ++ 算法: 解决初始选择种子点

步骤:
    先从我们的数据库随机挑个随机点当“种子点”。
    对于每个点，我们都计算其和最近的一个“种子点”的距离D(x)并保存在一个数组里，然后把这些距离加起来得到Sum(D(x))。
    然后，再取一个随机值，用权重的方式来取计算下一个“种子点”。这个算法的实现是，先取一个能落在Sum(D(x))中的随机值Random，然后用Random -= D(x)，直到其<=0，此时的点就是下一个“种子点”。
    重复第（2）和第（3）步直到所有的K个种子点都被选出来。
    进行K-Means算法。

http://rosettacode.org/wiki/K-means%2B%2B_clustering


"""

from com.kute.algorithms.kmeans.kmeans import Kmeans
import numpy as np
import random


class KmeansPlusPlus(Kmeans):

    def __init__(self, k, filepath):

        self.k = k
        self.filepath = filepath
        self.seedloclist = []

        Kmeans.__init__(self, k, filepath, None)

        # 挑选 种子点
        self.seedlocarray = self._select_seed()

    def _select_seed(self):
        # 先随机选一个种子点
        self.seedloclist.append(self.nlocationarray[np.random.choice(self.shape[0], 1, replace=False)][0])

        for seednum in range(1, self.k):
            distancesum = 0.0
            dotdistancemap = {}
            for dotindex, dotloc in enumerate(self.nlocationarray):

                distancedotseedmap = {}  # 存储 点群与所有的种子点的距离
                for seedindex, seedloc in enumerate(self.seedloclist):
                    distancedotseedmap[seedindex] = self._euclidean_distance(dotloc, seedloc)
                mindistancekey = min(distancedotseedmap, key=distancedotseedmap.get)  # 与种子点距离最小的key
                mindistance = distancedotseedmap[mindistancekey]

                distancesum += mindistance
                dotdistancemap[dotindex] = mindistance

            randomvalue = distancesum * random.random()
            for idx, iddistance in dotdistancemap.items():
                if randomvalue - iddistance <= 0:
                    self.seedloclist.append(self.nlocationarray[idx])
                    break



        self.seedloclist = self.nlocationarray[np.random.choice(self.shape[0], 3, replace=False)]
        return np.array(self.seedloclist)


def main():
    print(random.random())
    # filepath = "two_dimension_location.txt"
    # plus = KmeansPlusPlus(4, filepath)
    # plus.start()
    # print(plus.resultmap)
    # plus.show_figure()


if __name__ == '__main__':
    main()
