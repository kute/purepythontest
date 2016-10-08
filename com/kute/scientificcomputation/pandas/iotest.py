#! /usr/bin/env python
# -*- coding: utf-8 -*-

# __author__ = 'kute'
# __mtime__ = '16/9/24 17:29'

"""

"""


# %matplotlib inline

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd.set_option('display.mpl_style', 'default') # Make the graphs a bit prettier
plt.style.use = 'ggplot'
plt.rcParams['figure.figsize'] = (15, 5)


def main():
    try:
        # data = pd.read_csv('2012.csv', sep=",", encoding="utf8", parse_dates=['Date'], dayfirst=False, index_col='Date')
        # # print(data['pp'])
        # data['pp'].plot()
        ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', periods=1000))
        ts = ts.cumsum()
        ts.cumsum()










    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
