# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/6/25'
"""
import math
import geopy
from geopy.distance import great_circle
import pandas as pd
from shapely.wkb import dumps, loads
from shapely.wkt import dumps, loads
import pandas as pd
from shapely.geometry import MultiPoint
import os.path
import numpy as np
import os
from shapely.ops import cascaded_union


def destination(longitude, latitude, bearing, distance):
	lat1 = math.radians(latitude)
	lng1 = math.radians(longitude)
	bearing = math.radians(bearing)
	R = geopy.distance.EARTH_RADIUS
	d_div_r = (distance / R / 1000)
	lat2 = math.asin(
		math.sin(lat1) * math.cos(d_div_r) +
		math.cos(lat1) * math.sin(d_div_r) * math.cos(bearing)
	)
	lng2 = lng1 + math.atan2(
		math.sin(bearing) * math.sin(d_div_r) * math.cos(lat1),
		math.cos(d_div_r) - math.sin(lat1) * math.sin(lat2)
	)
	return math.degrees(lat2), math.degrees(lng2)


def getPoint(longitude, latitude, shipLength, shipWidth, angle):
	distance = math.sqrt(math.pow(shipLength / 2, 2) + math.pow(shipWidth / 2, 2))
	bearing = angle
	return destination(longitude, latitude, bearing, distance)


def getjiao(angle, ship_length, ship_width):
	math.degrees(math.atan(ship_width / ship_length))
	return (angle - math.degrees(math.atan(ship_width / ship_length)),
			angle + math.degrees(math.atan(ship_width / ship_length)))


angle1, angle2 = (getjiao(60, 200, 32))

###############生成泊位多边形的四个顶点坐标值##################################
print('###############生成泊位多边形的四个顶点坐标值##################################')
listpolygon = []
df = pd.DataFrame()
# df = pd.read_csv('Polygon/halfYearsaideberthlenwid.txt', header=None)
# df = pd.read_csv('Polygon/SGLonlatLengWidHead2.txt', header=None)
df = pd.read_csv('Polygon/port1lenwidhead7-6', header=None)
for i in range(len(df)):
	lon = df.iloc[i, 0]
	lat = df.iloc[i, 1]
	head = df.iloc[i, 2]
	shiplen = df.iloc[i, 3]
	shipwid = df.iloc[i, 4]
	angle1, angle2 = getjiao(head, shiplen, shipwid)
	A_lat, A_lon = getPoint(lon, lat, shiplen, shipwid, angle1)
	B_lat, B_lon = getPoint(lon, lat, shiplen, shipwid, angle2)
	C_lat, C_lon = getPoint(lon, lat, shiplen, shipwid, angle1 + 180)
	D_lat, D_lon = getPoint(lon, lat, shiplen, shipwid, angle2 + 180)
	# print(i,A_lon, A_lat, B_lon, B_lat, C_lon, C_lat, D_lon, D_lat)
	# print('POLYGON  ((',round(A_lon,8), round(A_lat,8),',',round(B_lon,8), round(B_lat,8),',', round(C_lon,8), round(C_lat,8),',', round(D_lon,8), round(D_lat,8),
	# 	  ',',round(A_lon,8), round(A_lat,8),'))')
	liststr = ['POLYGON  ((', str(A_lon), ' ', str(A_lat), ',', str(B_lon), ' ', str(B_lat), ',', str(C_lon), ' ',
			   str(C_lat), ',',
			   str(D_lon), ' ', str(D_lat), ',', str(A_lon), ' ', str(A_lat), '))', ]
	print(liststr)
	polygonstr = ''.join(liststr)
	print(polygonstr)
	wkt4 = loads(polygonstr)
	print('new  wkt4', wkt4)
	print(type(wkt4))
	listpolygon.append(wkt4)
print('多边形列表中的数目是', len(listpolygon))
for p in listpolygon:
	print(p)

###############合并泊位多边形##################################
print('###############合并泊位多边形##################################')
n = len(listpolygon)
print('n---------', n)
i = 0
while (i < n):
	a = listpolygon[i]
	for j in range(i + 1, n):
		b = listpolygon[j]
		if (a != None and b != None and a.intersects(b)):
			pyo = a.intersection(b)
			if ((pyo.area / a.area) > 0.2 or (pyo.area / b.area) > 0.2):
				print('相交区域的交集是', pyo)
				print('需要合并', i, j, a, b)
				# u = pyo.minimum_rotated_rectangle  # 此处需要改进
				# u = pyo.envelope # 改进1，求相交区域的边界再求外包矩形
				# u = pyo.convex_hull.minimum_rotated_rectangle  #改进2，求相交区域的凸包再求外包矩形
				# u = cascaded_union([a, b]).convex_hull.minimum_rotated_rectangle
				# print('相交区域的最小外包多边形是', u)
				if(b.area>=a.area):
					listpolygon[i] = b
					a = b
					listpolygon[j] = None
					b = None
				# listpolygon.append(u)
				else:
					listpolygon[j] = None
					b = None
				print('\n')
	i = i + 1  # print(listpolygon)
print('合并后的凸包的数目是', len(listpolygon))

################合并后的多边形写入到文本文件中##################################
print('===========合并后的多边形写入到文本文件中======================')
lsl = len(listpolygon)
print('合并后的泊位多边形数目是:', lsl)
with open('amstanPolygontest7-6', 'w') as f:
	for i in range(lsl):
		if (listpolygon[i] != None):
			# print(listpolygon[i])
			f.write(str(listpolygon[i]) + ";" + "Amsterdamv7" + ";" + str(listpolygon[i].centroid.x) + " " +
					str(listpolygon[i].centroid.y) + "\n")
