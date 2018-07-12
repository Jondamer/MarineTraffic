from shapely.ops import cascaded_union, polygonize
from scipy.spatial import Delaunay
import pylab as pl
from descartes import PolygonPatch
from shapely.geometry import MultiLineString
from numpy import asarray
import numpy as np
import shapely.geometry as geometry
import pandas as pd
import math
import pylab as plt
import os
import os.path
import shutil

# import matplotlib.pyplot as plt
# 过滤值为
alpha = 10
inDataPath = 'inData/'
outputdir = 'outDataBoundary/'
outputdir2 = 'convex_hullPolygon/'
edgePoints = pd.DataFrame()
edges = set()
# pointI = set()

coordinates = pd.DataFrame()
for parent, dirnames, filenames in os.walk(inDataPath):
	for filename in filenames:
		coordinates = coordinates.append(pd.read_csv(inDataPath + filename, header=None), ignore_index=True)
points = np.array(coordinates)

shutil.rmtree('outDataBoundary/')
shutil.rmtree('convex_hullPolygon/')
os.mkdir(outputdir)
os.mkdir(outputdir2)


def add_edge(edges, edgePointsPoly, points, i, j):
	"""
	Add a line between the i-th and j-th points,
	if not in the list already
	"""
	if (i, j) in edges or (j, i) in edges:
		return
	edges.add((i, j))
	edgePointsPoly.append(points[[i, j]])  # 这个地方设计的很巧妙


# print('==========================', points[i], points[j], points[[i, j]])


def alpha_shape(points, alpha):
	"""
	compute the alpha shape (concave hull) of a set of points.
	@param points: Iterable container of points
	@param alpha: alpha value to influence the gooeyness of the border. Smaller numbers 
	don't fall inward as much as larger numbers.
	Too large, and you lose everything!
	"""
	if len(points) < 4:
		return geometry.MultiPoint(list(points)).convex_hull

	tri = Delaunay(points)
	edges = set()
	edgePointsPoly = []
	# loop over triangles:
	# ia, ib, ic = indices of corner points of the triangle
	# for ia, ib, ic in tri.vertices:
	for ia, ib, ic in tri.simplices:
		# print('type(ia)', type(ia), ia, ib, ic)
		pa = points[ia]
		pb = points[ib]
		pc = points[ic]
		# Lengths of sides of triangle
		a = math.sqrt((pa[0] - pb[0]) ** 2 + (pa[1] - pb[1]) ** 2)
		b = math.sqrt((pb[0] - pc[0]) ** 2 + (pb[1] - pc[1]) ** 2)
		c = math.sqrt((pc[0] - pa[0]) ** 2 + (pc[1] - pa[1]) ** 2)
		# Semiperimeter of triangle
		s = (a + b + c) / 2.0
		# Area of triangle by Heron's formula
		area = math.sqrt(s * (s - a) * (s - b) * (s - c))
		circum_r = a * b * c / (4.0 * area)
		## Here's the radius filter
		if ((circum_r <= 1.0 / alpha)):
			add_edge(edges, edgePointsPoly, points, ia, ib)
			add_edge(edges, edgePointsPoly, points, ib, ic)
			add_edge(edges, edgePointsPoly, points, ic, ia)
		# print('列表edgePointsPoly',edgePointsPoly)
		# for i in edgePointsPoly:
		# print('=========',i)
	m = geometry.MultiLineString(edgePointsPoly)
	print('the number of LineString:', len(m))
	# for k in m:
	# 	print('+++++++++',k)
	# outputdir = outDataBoundaryPath2
	triangles = list(polygonize(m))  # triangles 上图观察
	print('the number of triangles:', len(triangles))
	# num = 1
	# for t in triangles:
	# 	# print('t是：', t)
	# 	# print('t的面积', t.area)
	# 	# if (t.area < 0.0010):
	# 	# 	continue
	# 	# s=t.convex_hull
	# 	# ar = asarray(t.exterior.coords)
	# 	ar = asarray(t.exterior.coords)
	# 	# if (len(ar) < 5):
	# 	# 	continue
	# 	fr = open(outputdir + 'triangles' + str(num) + '.txt', 'a')
	# 	num = num + 1
	# 	for e in ar:
	# 		fr.write(str(e[0]) + ',' + str(e[1]) + '\n')
	# 	fr.close()
	polygons = cascaded_union(triangles)  # 有交集的三角形进行合并得到一个合并生成的多边形集合
	print('After union,the number of polygons:', len(polygons))

	num = 1
	for t in polygons:
		if (t.area < 0.00005):
			continue
		ar = asarray(t.exterior.coords)
		fr = open(outputdir + 'exteriors-' + str(num) + '.txt', 'w')
		num = num + 1
		for e in ar:
			fr.write(str(e[0]) + ',' + str(e[1]) + '\n')
		fr.close()
	k = 1
	for t in polygons:
		# if (t.area < 0.0010):
		# 	continue
		s = t.convex_hull
		if s.area < 0.00350:
			continue
		# s = t.convex_hull.minimum_rotated_rectangle
		s = t.convex_hull.centroid.buffer(0.1, resolution=16, cap_style=1, join_style=1, mitre_limit=5.0)
		ar = asarray(s.exterior.coords)
		fr = open(outputdir2 + 'convex_hull-' + str(k) + '.txt', 'w')
		k = k + 1
		for e in ar:
			fr.write(str(e[0]) + ',' + str(e[1]) + '\n')
		fr.close()
	return polygons


# 调用函数alpha_shape
concave_hull = alpha_shape(points, alpha)
