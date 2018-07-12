# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/6/7'
"""
from shapely.geometry import MultiPoint
from shapely.geometry import Point
import numpy as np
import pandas as pd

out_df = pd.DataFrame()
data = pd.read_csv('outPut/6MonthIMOxibo-singaporePOI', header=None)
data.columns = ['lon', 'lat', 'num']
data = data[data.num >= 0]
# 排序
data.sort_values(by=['num'], ascending=False)
print(data.head(10))
max2 = data['num'].max()
print(type(max2))
print(max2)
maxnum = int(max2)
print(maxnum)
for j in range(maxnum):
	out_df = data[data['num'] == j]
	out_df.to_csv('singaporePOICu/' + 'cu' + "-" + str(j), index=False, header=False)
