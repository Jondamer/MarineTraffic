#-*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/3/30'
"""
import numpy as np
from shapely.geometry import Polygon
from shapely.geometry import multipoint
point = []
file = open('D:/zzt/001/test001.txt','r+')
for line in file.readlines():
    temp = line.strip().split(' ')
    lat = temp[0][4::]
    lng = temp[2][4::]
    point.append((lat,lng))
poly = Polygon((float(point[j][1]),float(point[j][0])) for j in range(len(point)))
print(poly)