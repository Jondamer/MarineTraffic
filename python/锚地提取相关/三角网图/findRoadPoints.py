from shapely.ops import cascaded_union, polygonize
from scipy.spatial import Delaunay
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
#import matplotlib.pyplot as plt
# 过滤值为
alpha = 100
inDataPath = 'inData/'
outDataPointsPath = 'outDataPoints/'
outDataBoundaryPath = 'outDataBoundary/'

##def plot_polygon(polygon):
##    fig = pl.figure(figsize=(10,10))
##    ax = fig.add_subplot(111)
##    margin = .3
##    x_min, y_min, x_max, y_max = polygon.bounds
##    ax.set_xlim([x_min-margin, x_max+margin])
##    ax.set_ylim([y_min-margin, y_max+margin])
##    patch = PolygonPatch(polygon, fc='#999999',
##                         ec='#000000', fill=True,
##                         zorder=-1)
##    ax.add_patch(patch)
##    return fig
edgePoints = pd.DataFrame()
def alpha_shape(points,alpha):
	"""
	compute the alpha shape (concave hull) of a set of points.
	@param points: Iterable container of points
	@param alpha: alpha value to influence the gooeyness of the border. Smaller numbers 
	don't fall inward as much as larger numbers.
	Too large, and you lose everything!
	"""
	if len(points) < 4 :
		return geometry.MultiPoint(list(points)).convex_hull
	def add_edge(edges,  edgePointsPoly, coords, i, j):
		"""
		Add a line between the i-th and j-th points,
		if not in the list already
		"""
		if (i,j) in edges or (j,i) in edges:
			return 
		edges.add((i,j))
		edgePointsPoly.append(coords[[i,j]])
		global edgePoints
		
		if(i not in pointI):
                        edgePoints = edgePoints.append([[points[i][0],points[i][1]]])
                        pointI.add(i)
		if(j not in pointI):
                        edgePoints = edgePoints.append([[points[j][0],points[j][1]]])
                        pointI.add(j)
               
		

	edges = set()
	pointI = set()
	edgePointsPoly = []
	tri = Delaunay(points)
	for ia, ib, ic in tri.vertices:
		pa = points[ia]
		pb = points[ib]
		pc = points[ic]

		# Lengths of sides of triangle
		a = math.sqrt((pa[0]-pb[0])**2 + (pa[1]-pb[1])**2)
		b = math.sqrt((pb[0]-pc[0])**2 + (pb[1]-pc[1])**2)
		c = math.sqrt((pc[0]-pa[0])**2 + (pc[1]-pa[1])**2)
		# Semiperimeter of triangle
		s = (a + b + c)/2.0

		delta = s*(s-a)*(s-b)*(s-c)

		if(delta>0):
		# Area of triangle by Heron's formula
##                    try:
                    area = math.sqrt(delta)
##                    except ValueError:
##                        continue
                    circum_r = a*b*c/(4.0*area)
                    ## Here's the radius filter
                    if((circum_r <= 1/alpha )):
                            add_edge(edges,  edgePointsPoly, points, ia, ib)					
                            add_edge(edges,  edgePointsPoly, points, ib, ic)					
                            add_edge(edges,  edgePointsPoly, points, ic, ia)
                    
	m = geometry.MultiLineString(edgePointsPoly)
	triangles = list(polygonize(m))
	polygon = cascaded_union(triangles)     
	outputdir = outDataBoundaryPath
	num = 1
	for t in polygon:
            outer = cascaded_union(t)
            print(outer.area)
            if(outer.area<0.00050):
              continue
            ar = asarray(t.exterior.coords)
            if(len(ar)<5):
                continue
            fr = open(outputdir+'exteriors-'+str(num)+'.txt','a')
            num = num+1
            for e in ar:
                fr.write(str(e[0])+','+str(e[1])+'\n')
            # fr.write('\n')
            fr.close()
        
	return polygon,edgePoints

coordinates = pd.DataFrame()
for parent,dirnames,filenames in os.walk(inDataPath):
    for filename in filenames:
        coordinates = coordinates.append(pd.read_csv(inDataPath+filename,header=None),ignore_index=True)
points = np.array(coordinates)
concave_hull, edgePoints = alpha_shape(points,alpha)
edgePoints.to_csv(outDataPointsPath+'roadDataPoints',index=False,header=False)
##plt.figure()
##plt.title("alpha = 2.0 Hull")
##plt.gca().add_patch(PolygonPatch(concave_hull,alpha=0.5,fc='#999999',
##                         ec='#000000'))
##plt.gca().autoscale(tight=False)
##plt.show()
