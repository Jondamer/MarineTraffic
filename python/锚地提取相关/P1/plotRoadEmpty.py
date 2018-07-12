##author:Charles.L
##date:2017/11/8
##method:plot road,empty domains datas in each folder,every file is 'lng,lat' without header

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.colors as colors
import matplotlib.cm as cmx
import numpy as np
import os
import os.path
import time

ISOTIMEFORMAT = '%Y-%m-%d %H:%M:%S'
# define some random data that emulates your indeded code:
NCURVES = 20
np.random.seed(101)
curves = [np.random.random(20) for i in range(NCURVES)]
values = range(NCURVES)
jet = cm = plt.get_cmap('jet')
cNorm = colors.Normalize(vmin=0, vmax=values[-1])
scalarMap = cmx.ScalarMappable(norm=cNorm, cmap=jet)

lllon = 80
urlon = 160
lllat = 10.41
urlat = 60.44

# map = Basemap(projection='ortho',\
# 	    lat_0=(urlat+lllat)/2,lon_0=(urlon+lllon)/2,\
#             ##llcrnrlat=lllat ,urcrnrlat=urlat,\
#             ##llcrnrlon=lllon,urcrnrlon=urlon,\
#             rsphere=6371200.,resolution='l',area_thresh=10000)
# map.drawmapboundary(fill_color='#689CD2')
# map.drawstates()
# map.drawcoastlines(linewidth=0.25)
# map.drawcountries(linewidth=0.25)
# map.drawmeridians(np.arange(0,360,30))
# map.drawparallels(np.arange(-90,90,30))
# map.fillcontinents(color='#BF9E30',lake_color='#689CD2',zorder=0)

map = Basemap()
map.readshapefile('D:/zzt/PyWorkSpace/CHN_adm_shp/CHN_adm1', 'states', drawbounds=True)
# map.readshapefile('D:/zzt/PyWorkSpace/HKG_adm_shp/HKG_adm1', 'states', drawbounds=True, color='green')
# map.readshapefile('D:/zzt/PyWorkSpace/SGP_adm_shp/SGP_adm1', 'states', drawbounds=True, color='green', zorder=10)
# map.readshapefile('D:/zzt/PyWorkSpace/MYS_adm_shp/MYS_adm1', 'states', drawbounds=True)
# map.readshapefile('D:/zzt/PyWorkSpace/IDN_adm_shp/IDN_adm1', 'states', drawbounds=True, color='blue', zorder=True)
map.drawstates(linewidth=0.1, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
# map.drawcoastlines(linewidth=1.0, linestyle='solid', color='blue', antialiased=1, ax=None, zorder=None)
map.drawcountries()
# map.drawmapboundary()
# map.drawmapboundary()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
# map.drawlsmask(land_color='#BF9E30', ocean_color='w', lsmask=None, lsmask_lons=None, lsmask_lats=None, lakes=True, resolution='l',grid=5)
# map.fillcontinents(lake_color='#689CD2',zorder=0)
map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)


def mapshow(roadpath, convexhullpath):
	for parent, dirnames, filenames in os.walk(convexhullpath):
		for filename in filenames:
			convexhullDf = pd.read_csv(convexhullpath + filename, header=None)
			lon = np.array(convexhullDf[0][0:])
			lat = np.array(convexhullDf[1][0:])
			x, y = map(lon, lat)
			plt.plot(x, y, color='green',markersize=10,linewidth=3)

	for parent, dirnames, filenames in os.walk(roadpath):
		for filename in filenames:
			roadDf = pd.read_csv(roadpath + filename, header=None, error_bad_lines=False)
			lon = np.array(roadDf[0][0:])
			lat = np.array(roadDf[1][0:])
			x, y = map(lon, lat)
			plt.plot(x, y, color='red',markersize=12)
	plt.title('Anchor plot result')
	plt.show()


if __name__ == '__main__':
	mapshow('outDataBoundary/', 'convex_hullPolygon/')
