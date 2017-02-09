#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0
@ __author__: kute 
@ __file__: build_binary_search_tree.py
@ __mtime__: 2017/2/8 16:38

构建二叉搜索树并给以图示（见  ./show.png）

"""

import attr
from matplotlib import pyplot as plt

xaxis = {}
xyloc = []


@attr.s
class Node(object):
    data = attr.ib(default=None)
    left = attr.ib(default=None)
    right = attr.ib(default=None)

    # for build matplotlib
    rootloc = attr.ib(default=(1, 1), convert=tuple)

    def insert(self, data=None):
        if self.data:
            if self.data > data:
                if self.left is None:
                    xaxis[data] = (self.rootloc[0] - 1, self.rootloc[1] - 1)
                    xyloc.append([xaxis[self.data], xaxis[data]])
                    self.left = Node(data=data)
                else:
                    self.left.rootloc = xaxis[self.left.data]
                    self.left.insert(data)
            elif self.data < data:
                if self.right is None:
                    xaxis[data] = (self.rootloc[0] + 1, self.rootloc[1] - 1)
                    xyloc.append([xaxis[self.data], xaxis[data]])
                    self.right = Node(data=data)
                else:
                    self.right.rootloc = xaxis[self.right.data]
                    self.right.insert(data)
            else:
                raise ValueError("There should not be the same value[{}] in Binary Search Tree".format(data))
        else:
            self.data = data
            xaxis[data] = self.rootloc


def render_figure(bst=None):
    plt.title(r'Build Binary Search Tree')
    if not bst or not bst.data:
        plt.axis([0, 10, 0, 10])
        plt.annotate('It\'s a null tree', xy=(4, 6), xytext=(6, 8),
            arrowprops=dict(facecolor='black', shrink=0.05))
    else:
        # 设置 x, y值的区间
        l = list(xaxis.values())
        xmin, xmax = min(l, key=lambda t: t[0]), max(l, key=lambda t: t[0])
        ymin, ymax = min(l, key=lambda t: t[1]), max(l, key=lambda t: t[1])
        plt.axis(list(map(lambda x: x * 5, [xmin[0], xmax[0], ymin[1], ymax[1]])))

        # 画 线段
        for line in xyloc:
            plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]])
        # 画 点
        for line in xyloc:
            plt.plot([line[0][0], line[1][0]], [line[0][1], line[1][1]], 'ro')
        plt.show()


def main():
    l = [5, 3, 6, 1, 4]
    bst = Node()
    for i in l:
        bst.insert(i)
    print(bst)
    render_figure(bst)


if __name__ == "__main__":
    main()
