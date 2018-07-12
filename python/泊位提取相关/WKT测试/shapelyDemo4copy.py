# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/6/21'
"""
import pandas as pd
from shapely.geometry import Point
import os.path
import numpy as np
import os
from shapely.ops import cascaded_union
from shapely.geometry import Polygon
from shapely.geometry import box

from shapely.wkb import dumps, loads
from shapely.wkt import dumps, loads
import pandas as pd
from shapely.geometry import MultiPoint
import os.path
import numpy as np
import os
from shapely.ops import cascaded_union
from shapely.geometry import Polygon
from shapely.geometry import box

listpolygon = []
# file = open()

for line in open("test.txt"):
	# print line,  #python2 用法
	# print(line)
	# print(type(line))
	wkt4 = loads(line)
	# print('new  wkt4', wkt4)
	# print(type(wkt4))
	listpolygon.append(wkt4)
# 遍历list
# for i in listpolygon:
# 	# print(type(i))
# 	print(listpolygon[i])
# 	# print(p)
# print('合并前泊位的数目是：', len(listpolygon))

# ll = len(listpolygon)
# for i in range(ll):
# print(listpolygon[i])
# print(listpolygon[i],';','bohaiwan',';',listpolygon[i].boundary.centroid.x,listpolygon[i].boundary.centroid.y)

# print(listpolygon[770])
# print((listpolygon[770].centroid).x, (listpolygon[770].centroid).y)

# # 遍历凸包，并合并相交的凸包
# # 合并后的凸包的数目
n = len(listpolygon)
print('n---------', n)
i = 0
while (i < n):
	a = listpolygon[i]
	for j in range(i + 1, n):
		# print(i,j)
		# print(a)
		b = listpolygon[j]
		# print(i, j,a,b)
		if (a != None and b != None and a.intersects(b)):
			# print(a,b)
			pyo = a.intersection(b)
			print('相交区域的多边形是', pyo, pyo.centroid.x, pyo.centroid.y)
			if ((pyo.area / a.area) > 0.5 or (pyo.area / b.area) > 0.5):
				print('需要合并', i, j, a, b)
				u = pyo.minimum_rotated_rectangle
				print('相交区域的最小外包多边形是', u, u.centroid.x, u.centroid.y)
				listpolygon[i] = u
				listpolygon[j] = None
				# listpolygon.append(u)
				print('\n')
	i = i + 1  # print(listpolygon)
print('合并后的凸包的数目是', len(listpolygon))

# 合并后的多边形写入到文本文件中
# print('=================================')
# for p in listpolygon:
# 	print(p)
print('=================================')
lsl = len(listpolygon)
print(lsl)
for i in range(lsl):
	if (listpolygon[i] != None):
		# print(listpolygon[i])
		print(listpolygon[i], ';', 'sgPolygon', ';', listpolygon[i].centroid.x, listpolygon[i].centroid.y)
