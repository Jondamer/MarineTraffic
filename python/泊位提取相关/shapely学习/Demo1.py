# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/6/12'
"""

import pandas as pd
from shapely.geometry import MultiPoint
import os.path
import numpy as np
from shapely.ops import cascaded_union

polygon1 = MultiPoint([(1, 0), (1, 1), (0, 1)]).convex_hull
polygon2 = MultiPoint([(2, 0), (3, 0), (3, 1), (2, 1)]).convex_hull
polygon3 = MultiPoint([(2.5, 0), (4, 0), (2.5, 1), (4, 1)]).convex_hull
polygon4 = MultiPoint([(1, 0), (3, 0), (3, 1), (1, 1)]).convex_hull
polygon5 = MultiPoint([(2, 1), (2, 2), (3, 2)]).convex_hull

print(type(polygon2))
print(polygon2.area)
print(polygon3.area)
# 2 3多边形是否相交
# b = polygon2.contains(polygon3)
# print('2和3多边形的', b)
# c = polygon2.covers(polygon3)
# print('c', c)
# d = polygon3.crosses(polygon2)
# print('d', d)
#
# e = polygon2.disjoint(polygon3)
# print('e', e)
# f = polygon3.intersection(polygon2)
# print('f', f)
# g = polygon2.intersects(polygon3)
# print('g', g)
h = polygon3.intersects(polygon4)
print('h', h)
if (h):
	u = cascaded_union([polygon3, polygon4])
print(u.area)
# print(u.boundary)
# print(u.centroid)

# df = pd.read_csv('../cu2/cu-1', header=None)
# df = df.iloc[:, 0:2]
# train_data = np.array(df)  # np.ndarray()
# train_x_list = train_data.tolist()  # list
# # print(train_x_list)
# # print(type(train_x_list))
# points = MultiPoint(train_x_list)
# py1 = points.convex_hull
# print('py1的相关属性值')
#
# print(py1.area)
# print(py1.boundary)
# print('凸包的中心点数据',py1.centroid)

list1 = []
# list1.append(polygon4)
list1.append(polygon3)
list1.append(polygon2)
list1.append(polygon1)
m = 0
print('===================================')
while m < len(list1):
	print(list1[m])
	m = m + 1
print('===================================')
list2 = list1[:]
i = 0
while (i < len(list2)):
	for j in range(i + 1, len(list2)):
		if (list2[i].intersects(list2[j])):
			# print(list1[i],list1[j])
			print(list2[i], list2[j])
			u = cascaded_union([list2[i], list2[j]]).convex_hull
			if (list2[i] in list1):
				list1.remove(list2[i])
				print('在里面')
			if (list2[j] in list1):
				list1.remove(list2[j])
				print('在里面')
			list1.append(u)
	i = i + 1
print(list1)
print('合并后的凸包的数目是', len(list1))
print('===================================')
for k in range(len(list1)):
	print(list1[k])
	print(list1[k].centroid)
print('===================================')
