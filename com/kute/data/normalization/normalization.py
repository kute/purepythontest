#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/3/1 21:07'

"""

常见归一化 方法

https://www.biaodianfu.com/data-normalization.html

"""

import math
from matplotlib import pyplot as plt


class Normalization(object):

    def __init__(self, origindatalist=None):
        self.data = origindatalist

    def _maxv(self):
        return max(self.data)

    def _minv(self):
        return min(self.data)

    def _matplot(self, result=None):
        plt.figure(1)
        plt.subplot(2, 1, 1)
        plt.plot(self.data, 'ro')

        if result and len(result) > 0:
            plt.subplot(2, 1, 2)
            plt.plot(result, 'go')

        plt.show()

    def normal_min_max(self, maxv=None, minv=None, precious=8, showmat=False):
        """ Min-max normalization
        对原始数据的线性变换
        设minA和maxA分别为属性A的原始值中的最小值和最大值，
        将属性A的一个原始值v通过min-max标准化映射成在区间[new_minA, new_maxA]中的值v’的计算方法是:

        v' = (v - minA) * (new_maxA - new_minA) / (maxA - minA) + new_minA

        若区间为[0, 1], 则公式简化为

        v' = (v - minA) / (maxA - minA)

        min-max标准化方法保留了原始数据之间的相互关系，
        但是如果标准化后，新输入的数据超过了原始数据的取值范围，
        即不在原始区间[minA, maxA]中，则会产生越界错误。
        因此这种方法适用于原始数据的取值范围已经确定的情况

        :param maxv: 原始数据的最大值
        :param minv: 原始数据的最小值
        :param precious: 规格化后的数据精度,默认8

        """
        maxv = maxv or self._maxv()
        minv = minv or self._minv()
        gapv = maxv - minv
        precious = precious or 8

        result = []
        for ele in self.data:
            result.append(round((ele - minv) / gapv, precious))

        if showmat:
            self._matplot(result)
        return result

    def normal_z_score(self, precious=8, showmat=False):
        """ 0 均值规格化  zero-mean normalization
        这种方法基于原始数据的均值(mean)和标准差(standard deviation)进行数据的标准化。
        经过处理的数据符合标准正态分布，即均值为0，标准差为1
        将属性A的原始值v使用z-score标准化到v’的计算方法是

        v' = (v - uA) / ∂A

        其中 uA 表示 平均值, ∂A 表示标准方差(方差平方根)

        推导:
        uA = (x1 + x2 + ... + xn) / n
        ∂A = [(x1 - uA)^2 + (x2 - uA)^2 + ... + (xn - uA)^2] / n

           = (x1^2 + x2^2 + ... + xn^2) / n - (x1 + x2 + ... + xn)^2 / n^2
        """
        s = 0
        s2 = 0
        n = len(self.data)
        for ele in self.data:
            s += ele
            s2 += ele * ele
        variance = s2 / n - s * s / (n * n)
        standard = math.sqrt(variance)
        mean = s / n
        result = []
        for ele in self.data:
            result.append(round((ele - mean) / standard, precious))
        if showmat:
            self._matplot(result)
        return result

    def normal_log(self, precious=8, showmat=False):
        """
        落到[0, 1]区间的公式为
        v' = math.log10(v) / math.log10(maxA)
        :param precious: 8

        """
        result = []
        maxv = self._maxv()
        precious = precious or 8
        logmaxv = math.log10(maxv)
        for ele in self.data:
            result.append(round(math.log10(ele) / logmaxv, precious))
        if showmat:
            self._matplot(result)
        return result

    def normal_atan(self, precious=8, showmat=False):
        """
        反正切函数
        v' = math.atan(v) * 2 / math.pi

        使用这个方法需要注意的是如果想映射的区间为[0,1]，则数据都应该大于等于0，小于0的数据将被映射到[-1,0]区间上
        """
        result = []
        precious = precious or 8
        for ele in self.data:
            result.append(round(math.atan(ele) * 2 / math.pi, precious))
        if showmat:
            self._matplot(result)
        return result


def main():
    data = [3, 5, 8, 2, 6, 7, 9]
    normal = Normalization(data)
    print(normal.normal_min_max())
    print(normal.normal_log())
    print(normal.normal_atan())
    print(normal.normal_z_score(showmat=True))


if __name__ == '__main__':
    main()
