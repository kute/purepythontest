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


"""

from com.kute.algorithms.kmeans.kmeans import Kmeans


class KmeansPlus(Kmeans):

    def __init__(self, k, filepath, seedloc):

        self.k = k
        self.filepath = filepath
        self.seedloc = seedloc or self._select_seed()

        Kmeans.__init__(self, k, filepath, seedloc)

    def _select_seed(self):
        return []


def main():
    filepath = "two_dimension_location.txt"
    plus = KmeansPlus(4, filepath, None)
    print(plus.resultmap)
    plus.show_figure()


if __name__ == '__main__':
    main()
