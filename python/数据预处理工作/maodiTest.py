# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/3/30'
"""
import numpy as np
from shapely.geometry import Polygon

point = []
point2 = []
PY = []
# temp=[]
file = open('D:/zzt/001/cdays-4-result2.txt', 'r+')
for line in file.readlines():
	if (line.startswith('o')):
		continue
	temp = line.strip().split(' ')
	lat = temp[0][4::]
	lng = temp[2][4::]
	point.append((lat, lng))
# print(len(point))
# if line.startswith('o'):  # continue
# print(len(point))
# print(len(PY))
# poly = Polygon((float(point[j][1]), float(point[j][0])) for j in range(len(point)))
# print(poly)
# point.clear()  #重新清空
