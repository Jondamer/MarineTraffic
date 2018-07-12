# coding=UTF-8
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

data = pd.DataFrame()
data2 = pd.DataFrame()
# 一个月所有船只类型一带一路区域的数据上图
# filepath = 'D:/zzt/02MonthALLShipsPOI24bitsGrided00/'

# 一年的一带一路区域的数据上图展示
# filepath = 'D:/zzt/OneWayOneRoad/oneYear-5/'

# 半年的一带一路区域的数据上图展示
# filepath =  'D:/zzt/OneWayOneRoad/7_12Month/'

# 一个月的全球的数据上图展示（含一带一路区域）
# filepath='D:/zzt/GLOBALIMOPOI/9MonthIMOPOI24bitsGrided/'

# filepath='D:/zzt/GLOBALIMOPOI/5MonthIMOPOI20bitsGrided/'
# 锚地数据图
filepath = 'BerthData/'
filepath2 = 'AnchorData/'
# 核密度指数的值
# filepath='D:/zzt/HemiduzhishuEXT2/'

# D:\航海项目\数据相关\泊位最新数据\Test100 singapore-indianIMO-678DATA
# filepath = 'D:\北工大郑振涛\航海项目\数据相关\停留点数据栅格化\shanghaiHongkong24BitsGridV2\'
# filepath = 'D:/航海项目/数据相关/泊位最新数据/singapore-indianIMO-678DATA/'
# filepath = 'E:/航海项目/数据相关/油轮数据/TankerByMonth/060708/outData/'
for parent, dirnames, filenames in os.walk(filepath):
	for filename in filenames:
		f = filepath + filename
		# print(filepath + filename)
		print(f)
		# print(os.path.getsize(filepath+filename))
		# # 添加判断条件，如果文件大小为0的话则删除此文件
		# if(os.path.getsize(filepath+filename)==0):
		#     os.remove(filepath+filename)
		data = data.append(pd.read_csv(filepath + filename, header=None))

for parent, dirnames, filenames in os.walk(filepath2):
	for filename in filenames:
		f2 = filepath2 + filename
		# print(filepath + filename)
		print(f2)
		# print(os.path.getsize(filepath+filename))
		# # 添加判断条件，如果文件大小为0的话则删除此文件
		# if(os.path.getsize(filepath+filename)==0):
		#     os.remove(filepath+filename)
		data2 = data2.append(pd.read_csv(filepath2 + filename, header=None))

#
# lllon = 80
# urlon = 160
# lllat = 10.41
# urlat = 60.44


map = Basemap()
# map = Basemap(projection='cyl', resolution=None,
#             llcrnrlat=-90, urcrnrlat=90,
#             llcrnrlon=-180, urcrnrlon=180, )
# map=Basemap(projection='mill')
map.readshapefile('D:/zzt/PyWorkSpace/CHN_adm_shp/CHN_adm1', 'states', drawbounds=True)
map.readshapefile('D:/zzt/PyWorkSpace/HKG_adm_shp/HKG_adm1', 'states', drawbounds=True)
map.readshapefile('D:/zzt/PyWorkSpace/SGP_adm_shp/SGP_adm1', 'states', drawbounds=True)
map.readshapefile('D:/zzt/PyWorkSpace/MYS_adm_shp/MYS_adm1', 'states', drawbounds=True)
map.readshapefile('D:/zzt/PyWorkSpace/IDN_adm_shp/IDN_adm1', 'states', drawbounds=True)
# map.readshapefile('D:/PyWorkSpace/CHN_adm_shp/CHN_adm1', 'states', drawbounds=True)
# map.readshapefile('D:/PyWorkSpace/航海项目/MYS_adm_shp/MYS_adm1', 'states', drawbounds=True,color='blue')
# map.readshapefile('D:/PyWorkSpace/航海项目/SGP_adm_shp/SGP_adm1', 'states', drawbounds=True,color='red')
# map.readshapefile('D:/PyWorkSpace/航海项目/IDN_adm_shp/IDN_adm1', 'states', drawbounds=True,color='blue')
# map.readshapefile('D:/PyWorkSpace/航海项目/LKA_adm_shp/LKA_adm1', 'states', drawbounds=True,color='blue')
# map.readshapefile('D:/PyWorkSpace/航海项目/IND_adm_shp/IND_adm1', 'states', drawbounds=True,color='blue')

map.drawstates(linewidth=0.1, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
# map.drawcoastlines(linewidth=1.0, linestyle='solid', color='blue', antialiased=1, ax=None, zorder=None)
map.drawcountries()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)


# map.fillcontinents(color='coral',lake_color='#689CD2',zorder=0)
def mapshow():
	##	filter v1 lon,lat in defined range

	# posi_fea = pd.read_csv(feature_filepath + suffix, header=None)
	# 添加判断条件

	posi_fea = data
	print(posi_fea.shape)
	lon = np.array(posi_fea[2][1:])
	lat = np.array(posi_fea[3][1:])
	# size = 3
	size = 4
	# ax = plt.gca()
	x, y = map(lon, lat)
	map.scatter(x, y, s=size, color='red')
	# ax.plot(lon,lat,marker=None,color='m')
	posi_fea2 = data2
	print(posi_fea2.shape)
	lon2 = np.array(posi_fea2[2][1:])
	lat2 = np.array(posi_fea2[3][1:])
	# size = 3
	size = 4
	# ax = plt.gca()
	x2, y2 = map(lon2, lat2)
	map.scatter(x2, y2, s=size, color='green')
	# ax.plot(lon,lat,marker=None,color='m')


	plt.title('Stop Data ')
	plt.show()


if __name__ == '__main__':
	mapshow()
	print('END TIME', time.strftime(ISOTIMEFORMAT, time.localtime()))
