#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/2/5 22:24'

"""
http://matplotlib.org/users/gridspec.html
布局

"""

import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from pylab import mpl
# 中文字体设置
mpl.rcParams['font.sans-serif'] = ['SimHei']
# - 符号显示为方块问题
mpl.rcParams['axes.unicode_minus'] = False


def main():

    # subplot 布局
    subplot2grid_test()

    # 另一种实现
    # gridspec_test()

    # subplotspec
    # subplotspec_test()


def subplotspec_test():
    gs = gridspec.GridSpec(2, 1)

    gs0 = gridspec.GridSpecFromSubplotSpec(1, 3, subplot_spec=gs[0])
    # set ax1
    ax1 = plt.subplot(gs0[:, :])
    plt.title(r'ax111')

    gs1 = gridspec.GridSpecFromSubplotSpec(2, 3, subplot_spec=gs[1])
    # set ax2, ax3, ax4, ax5
    ax2 = plt.subplot(gs1[0, : 2])
    plt.title(r'ax222')
    ax3 = plt.subplot(gs1[:, 2])
    plt.title(r'ax333')
    ax4 = plt.subplot(gs1[1, 0])
    plt.title(r'ax444')
    ax5 = plt.subplot(gs1[1, 1])
    plt.title(r'ax555')

    plt.show()


def gridspec_test():
    gs = gridspec.GridSpec(3, 3)
    # gs.update(left=0.05, right=0.48, wspace=0.05)

    # 使用切片来实现 colspan rowspan
    ax1 = plt.subplot(gs[0, :])
    plt.title(r'ax11')

    ax2 = plt.subplot(gs[1, 0: 2])
    # ax2 = plt.subplot(gs[1, 0: -1])
    plt.title(r'ax22')

    ax3 = plt.subplot(gs[1:, 2])
    # ax3 = plt.subplot(gs[1:, -1])
    plt.title(r'ax33')

    ax4 = plt.subplot(gs[2, 0])
    # ax4 = plt.subplot(gs[-1, 0])
    plt.title(r'ax44')

    ax5 = plt.subplot(gs[2, 1])
    # ax5 = plt.subplot(gs[-1, -2])
    plt.title(r'ax55')

    plt.show()


def subplot2grid_test():
    """左: x axis
       右: y axis
    """
    shape = (3, 3)
    ax1 = plt.subplot2grid(shape, (0, 0), colspan=3)
    plt.title(r'ax1')
    ax2 = plt.subplot2grid(shape, (1, 0), colspan=2)
    plt.title(r'ax2')
    ax3 = plt.subplot2grid(shape, (1, 2), rowspan=2)
    plt.title(r'ax3')
    ax4 = plt.subplot2grid(shape, (2, 0))
    plt.title(r'ax4')
    ax5 = plt.subplot2grid(shape, (2, 1))
    plt.title(r'ax5')

    plt.show()


if __name__ == '__main__':
    main()
