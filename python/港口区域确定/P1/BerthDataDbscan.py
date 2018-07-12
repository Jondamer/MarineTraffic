# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/5/25'
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import DBSCAN
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
import os.path
from shapely.geometry import MultiPoint
import os.path
import numpy as np

# filepath = '6.28/saidexiboHalfYearPOI/'
# Data = pd.DataFrame()
# for parent, dirnames, filenames in os.walk(filepath):
# 	for filename in filenames:
# 		f = filepath + filename
# 		print(f)
# 		Data = Data.append(pd.read_csv(filepath + filename, header=None))

Data = pd.read_csv('bohaiwanxibo7-8-9monthPOICom/bohaiwanxibo7-8-9monthPOICom', header=None)
print(Data.head(10))
# Data.columns = ['utc', 'mmsi', 'lon', 'lat', 'status', 'length', 'width', 'head', 'v']
Data.columns = ['lon', 'lat', ]
Data.sort_values(by='lon')
print('Data的shape', Data.shape)
print(Data.head(10))
# 去除重复的数据,并按照经度数据降序排序
X1 = Data.iloc[:, 0:2].drop_duplicates()
# X1 = Data.iloc[1:500000, 2:4]
print('X1的shape', X1.shape)
# print(type(X1))
X1.columns = ['lon', 'lat']

X1 = X1.sort_values(by='lon')
# X1.sort_values(by='longitude')
print(X1.head(10))
X2 = X1.values

# print(type(X2))
# print(X2)
# X = StandardScaler().fit_transform(X1)

# Compute DBSCAN
coords = X1.as_matrix()
print('coords的形状', coords.size)
print('coords的形状', coords.shape)
print('coords的形状', len(coords))
kms_per_radian = 6371.0088
epsilon = 1 / kms_per_radian
db = DBSCAN(eps=epsilon * 0.002, min_samples=80, algorithm='ball_tree', metric='haversine', n_jobs=-1).fit(
	np.radians(coords))
# db = DBSCAN(eps=epsilon * 0.008, min_samples=70, algorithm='ball_tree', metric='haversine', n_jobs=-1).fit(
# 	np.radians(coords))

# db = DBSCAN(eps=0.0005, min_samples=25).fit(X)
core_samples_mask = np.zeros_like(db.labels_, dtype=bool)
core_samples_mask[db.core_sample_indices_] = True
labels = db.labels_

# Number of clusters in labels, ignoring noise if present.
n_clusters_ = len(set(labels)) - (1 if -1 in labels else 0)

print('Estimated number of clusters: %d' % n_clusters_)

# #############################################################################
# outPut lon lat  labels
y_pred = DBSCAN(eps=epsilon * 0.002, min_samples=80, algorithm='ball_tree', metric='haversine', n_jobs=-1).fit_predict(
	np.radians(coords))
A = pd.DataFrame(coords)
# A = Data
B = pd.DataFrame(y_pred)
#
out = pd.concat([A, B], axis=1)
print(out.shape)
out = pd.DataFrame(out)
# 删除含有空值的行
out = out.dropna(axis=0, how='any')
# 删除噪点数据，并按照簇号降序排序
# out.columns = ['utc', 'mmsi', 'lon', 'lat', 'status', 'length', 'width', 'head', 'v', 'num']
list1 = []
list2 = []
out.columns = ['lon', 'lat', 'num']

out.sort_values(by='num', ascending=True)
# df.sort_values(by='col1', ascending=False)
out = out[out['num'] >= 0.0]
out.to_csv('quzao', header=False, index=False)
max2 = out['num'].max()
print(type(max2))
print(max2)
maxnum = int(max2)
print(maxnum)
for j in range(maxnum):
	out_df = out[out['num'] == j]
	# out_df.to_csv('outPut/' + 'saidecu' + "-" + str(j), index=False, header=False)
	train_data = np.array(out_df)  # np.ndarray()
	train_x_list = train_data.tolist()  # list
	points = MultiPoint(train_x_list)
	list1.append(points.centroid.x)
	list2.append(points.centroid.y)
	# list 转变成DataFrame
	df1 = pd.DataFrame(list1)
	df2 = pd.DataFrame(list2)
	print(df1.shape)

	# 按列合并两个dataFrame ,并输出到文本文件中
	outs = pd.concat([df1, df2], axis=1)
	print(outs.shape)
	outs.to_csv('outPut/' + 'halfYearport1xiboPOIzhongxindian', header=False, index=False)

# out.to_csv('outPut/' + 'saidecu', header=False, index=False)

# #############################################################################
# Plot result
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
#
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
map.readshapefile('D:/zzt/PyWorkSpace/EGY_adm_shp/EGY_adm1', 'states', drawbounds=True)


map.drawstates(linewidth=0.1, linestyle='solid', color='k', antialiased=1, ax=None, zorder=None)
map.drawcoastlines(linewidth=0.1, linestyle='solid', color='blue', antialiased=1, ax=None, zorder=None)
map.drawcountries()
map.drawmeridians(np.arange(0, 360, 30))
map.drawparallels(np.arange(-90, 90, 30))
map.fillcontinents(color='#BF9E30', lake_color='#689CD2', zorder=0)
#
#
# # filepath2 = '6.28/saidexiboHalfYearPOI/'
# Data2 = pd.DataFrame()
# # for parent, dirnames, filenames in os.walk(filepath2):
# # 	for filename in filenames:
# # 		f2 = filepath2 + filename
# # 		# print(f2)
# # 		Data2 = Data2.append(pd.read_csv(filepath2 + filename, header=None))
# Data2 = pd.read_csv('port1xiboPOICobine/port1xiboPOICobine', header=None)
# posi_fea = Data2
# print(posi_fea.shape)
# lon = np.array(posi_fea[0][0:])
# lat = np.array(posi_fea[1][0:])
# size = 5
# # ax = plt.gca()
# x, y = map(lon, lat)
# map.scatter(x, y, s=size, color='green')
#
#
#
#


# Black removed and is used for noise instead.
unique_labels = set(labels)
colors = [plt.cm.Spectral(each)
		  for each in np.linspace(0, 1, len(unique_labels))]
for k, col in zip(unique_labels, colors):
	if k == -1:
		# Black used for noise.
		col = [0, 0, 0, 1]

	class_member_mask = (labels == k)
	xy = X2[class_member_mask & core_samples_mask]
	plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
			 markeredgecolor='k', markersize=10)

	# xy = X2[class_member_mask & ~core_samples_mask]
	# plt.plot(xy[:, 0], xy[:, 1], 'o', markerfacecolor=tuple(col),
			 # markeredgecolor='k', markersize=5)

plt.title('Estimated number of clusters: %d' % n_clusters_)
plt.show()
