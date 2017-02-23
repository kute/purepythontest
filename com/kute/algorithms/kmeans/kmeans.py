#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: kmeans.py
@ __mtime__: 2017/2/21 15:07

kmeans 二维点坐标 计算 图示

测试样本：two_dimension_location.txt

运行结果图见: kmeans-result.png

"""

import numpy as np
from matplotlib import pyplot as plt
from math import sqrt, pow
from collections import defaultdict

from pylab import mpl
# 中文字体设置
mpl.rcParams['font.sans-serif'] = ['SimHei']
# - 符号显示为方块问题
mpl.rcParams['axes.unicode_minus'] = False

np.random.seed(2017)


class Kmeans(object):

    def __init__(self, k, filepath, seedloc):
        if not filepath:
            raise ValueError("should special the file path.")
        self.k = k
        self.filepath = filepath
        self.nlocationarray = None
        self.linestyles = ['bo', 'ro', 'go', 'yo', 'ko', 'mo', 'co']

        self._load_txt()
        self.shape = self.nlocationarray.shape
        self.seedlocarray = seedloc or self._gen_seed()

        self.resultmap = defaultdict(list)

        self.start()

    def _gen_seed(self):
        """从样本中随机出k个点
        """
        indexary = np.random.choice(self.shape[0], size=self.k, replace=False)
        return self.nlocationarray[indexary]

    def _load_txt(self):
        """加载数据样本
        """
        with open(self.filepath) as fp:
            self.nlocationarray = np.loadtxt(fp, delimiter=",", dtype=float)
            # print(self.nlocationarray)
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
        for key, dotlist in self.resultmap.items():
            tdotlist = taskresultmap[key]
            dotarray = np.array(dotlist)
            tdotarray = np.array(tdotlist)
            dotarray.sort(axis=0)
            tdotarray.sort(axis=0)
            for index, subarray in enumerate(dotarray):
                if len(set(list(subarray)) - set(list(tdotarray[index]))) > 0:
                    return False
        return True

    def _determining_seed(self):
        """选取点群的中心点（点坐标取均值，精度6位）
        """
        if len(self.resultmap) > 0:
            newseedarray = []
            nresultarray = np.array(list(self.resultmap.values()))
            for subarray in nresultarray:
                dotarray = np.array(subarray)
                subnums = len(dotarray)
                x, y = [round(sum(dotarray[:, 0]) / subnums, 6), round(sum(dotarray[:, 1]) / subnums, 6)]
                newseedarray.append([x, y])
            self.seedlocarray = np.array(newseedarray)
            return True
        return False

    def show_figure(self):
        linestylearray = np.random.choice(self.linestyles, self.k + 1, replace=False)
        # print(linestylearray)
        plt.figure(1)
        plt.subplot(2, 1, 1)
        lines = plt.plot(self.nlocationarray[:, 0], self.nlocationarray[:, 1], linestylearray[0])
        plt.title("原始点群分布")
        plt.xlabel("x label")
        plt.ylabel("y label")
        # plt.figure(2)
        plt.subplot(2, 1, 2)
        for index, sublinelist in self.resultmap.items():
            sublinearray = np.array(sublinelist)
            plt.plot(sublinearray[:, 0], sublinearray[:, 1], linestylearray[index + 1])
        plt.title("聚类结果点群分布")
        plt.xlabel("x label")
        plt.ylabel("y label")
        plt.show()

    def start(self):
        taskresultmap = defaultdict(list)
        for location in self.nlocationarray:
            distancemap = {}
            for index, seedloc in enumerate(self.seedlocarray):
                distancemap[index] = self._euclidean_distance(location, seedloc)
            key_min_distance = min(distancemap, key=distancemap.get)
            taskresultmap[key_min_distance].append(location)
        if not self._is_closure(taskresultmap):
            self.resultmap = taskresultmap.copy()
            if self._determining_seed():
                self.start()

    @property
    def result(self):
        return self.resultmap


def main():
    filepath = "two_dimension_location.txt"
    kmeans = Kmeans(4, filepath, None)
    kmeans.start()
    print(kmeans.result)
    kmeans.show_figure()


if __name__ == "__main__":
    main()
