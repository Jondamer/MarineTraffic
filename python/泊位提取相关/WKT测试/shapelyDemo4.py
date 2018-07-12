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
# file = open("test.txt")

for line in open("sgPolygon.txt"):
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
list2py = listpolygon[:]
i = 0
while (i < len(list2py)):
	for j in range(i + 1, len(list2py)):
		a = list2py[i]
		b = list2py[j]
		# print(type(a))
		if (a.intersects(b)):
			pyo = a.intersection(b)
			if ((pyo.area / a.area) > 0.5 or (pyo.area / b.area) > 0.5):
				# print('需要合并', a, b)
				# u1 = cascaded_union([a, b]).convex_hull
				u = pyo.envelope
				# evp = u1.envelope  # 确保合并后的多边形是一个矩形
				if (a in listpolygon):
					listpolygon.remove(a)
				print('移出合并前的多边形a',a)
				if (b in listpolygon):
					listpolygon.remove(b)
				print('移出合并前的多边形b',b)
				print('\n')
				# print('u--', u.area)
				# print("evp--", evp.area)
				listpolygon.append(u)
	i = i + 1
print(listpolygon)
print('合并后的凸包的数目是', len(listpolygon))

# 合并后的多边形写入到文本文件中
# print('=================================')
# for p in listpolygon:
# 	print(p)
print('=================================')
lsl = len(listpolygon)
print(lsl)
for i in range(lsl):
# 	# print(listpolygon[i])
# 	# print(listpolygon[i],';','sgPolygon',';',listpolygon[i].boundary.centroid.x,listpolygon[i].boundary.centroid.y)
# 	print(listpolygon[i], ';', 'sgPolygon', ';', listpolygon[i].centroid.x, listpolygon[i].centroid.y)
	print(listpolygon[i].centroid.x, listpolygon[i].centroid.y)
