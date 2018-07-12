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

# points = MultiPoint([(0.0, 0.0), (1.0, 1.0)])
# print(points.centroid)

# 创建pandas
d = {'col1': [1, 2], 'col2': [3, 4]}
df1 = pd.DataFrame(data=d)
print(df1)

# dataFrame 转变成 list
train_data = np.array(df1)  # np.ndarray()
train_x_list = train_data.tolist()  # list
print(train_x_list)
print(type(train_x_list))

polygon = MultiPoint(train_x_list).convex_hull
print(polygon.centroid)

points = MultiPoint(train_x_list)
print('hhhh', points.centroid)

out_df = pd.DataFrame()
df = pd.read_csv('outPut/xiboPOIDbscan2_2', header=None)
df.columns= ['lon', 'lat', 'num']
print(df.head(10))
max2 = df['num'].max()
print(type(max2))
print(max2)
maxnum = int (max2)
print(maxnum)
for j in range(maxnum):
	out_df = df[df['num'] == j]
	out_df.to_csv('cu2/' + 'cu' + "-" + str(j), index=False, header=False)

