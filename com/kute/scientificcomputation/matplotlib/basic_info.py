#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '2017/1/30 19:45'

"""
基本用法概念

"""
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from math import e, sin, pi, tan

from pylab import mpl
# 中文字体设置
mpl.rcParams['font.sans-serif'] = ['SimHei']
# - 符号显示为方块问题
mpl.rcParams['axes.unicode_minus'] = False


def main():
    print(matplotlib.__version__)

    # 渲染 幂函数
    # render_fx()

    # 多个图表
    # render_mutil_charts()

    # 处理数学表达式
    # render_mathematical_expression()

    # 双曲函数
    run_hyperbolic()


def run_hyperbolic():
    x = np.arange(-10, 10)
    # plt.plot(x, np.tanh(x))

    plt.figure(1)

    a = [[1, 1], [1, 0]]
    b = [[1, 1], [1, 0]]

    plt.plot(np.tanh(a + b))

    plt.show()


def render_mathematical_expression():
    """
    http://matplotlib.org/users/mathtext.html#mathtext-tutorial
    http://matplotlib.org/users/mathtext.html#symbols
    """
    x = np.arange(0.0, 15.0, 0.03)
    plt.plot(x, np.cos(2*np.pi*x) * 20)
    plt.ylim(-60, 60)  # 限制大小

    plt.title(r'$\alpha > \beta$')  # α > β

    mathtext = [
        r'$\alpha > \beta$',
        r'\$5.0-\$7.889',
        r'$\alpha_i > \beta_i$',
        r'$\sum_{i=0}^\infty x_i$',
        r'{[5 * (6 + 2)] / 4}',
        r'$\frac{3}{4} \binom{3}{4} \stackrel{3}{4}$',
        r'$(\frac{5 - \frac{1}{x}}{4})$',
        r'$\left(\frac{5 - \frac{1}{x}}{4}\right)$',
        r'$\sqrt{2}$',
        r'$\sqrt[3]{x}$',
        r'$s(t) = \mathcal{A}\sin(2 \omega t)$'
    ]

    length = len(mathtext)
    for i in range(1, length + 1):
        plt.text(0, (i - 1) * 5, mathtext[i - 1])

    # 在制定位置添加注释(也可以用text)
    plt.annotate('local mask', xy=(8, 20), xytext=(10, 30),
            arrowprops=dict(facecolor='black', shrink=0.05),)
    plt.show()


def render_mutil_charts():

    plt.figure(1)                # the first figure, 第一个图表(弹窗)
    # the first subplot in the first figure, 第一个弹窗里的第一个图,相当于 plt.subplot(2, 1, 1), 2行1列索引为1
    plt.subplot(211)
    plt.plot([1, 2, 3])
    plt.subplot(2, 1, 2)             # the second subplot in the first figure
    x = np.arange(1, 100)
    plt.plot(x, np.sinh(x))

    plt.figure(2)                # a second figure
    # plt.plot([4, 5, 6])          # creates a subplot(111) by default
    np.random.seed(19680801)

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # 直方图
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)
    plt.grid(True)
    plt.title(r"$\sigma_i=15$")

    plt.figure(1)                # figure 1 current; subplot(212) still current
    plt.subplot(211)             # make subplot(211) in figure1 current
    plt.title(r'Easy as 1, 2, 3')  # subplot 211 title
    plt.show()


def render_fx():

    #  api以及线条样式:  http://matplotlib.org/api/pyplot_api.html#matplotlib.pyplot.plot
    plt.plot([sin(2 * y) for y in range(-10, 10)], 'r--', linewidth=2.0)

    xaxis = [x for x in range(-10, 10)]
    yaxis = [tan(2 * x) for x in range(-10, 10)]
    lines = plt.plot(xaxis, yaxis, 'b:')
    # 设置线条样式:  http://matplotlib.org/users/pyplot_tutorial.html#controlling-line-properties
    plt.setp(lines, 'color', 'b', 'linewidth', '4.0')

    # 限制x y大小
    plt.axis([-10, 20, -1, 1])

    plt.ylabel("y axis")
    plt.xlabel("x axis")
    plt.show()

if __name__ == '__main__':
    main()
