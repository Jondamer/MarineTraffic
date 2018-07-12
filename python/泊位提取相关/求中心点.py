# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/6/7'
"""

import pandas as pd
from shapely.geometry import MultiPoint
import os.path
import numpy as np

# 定义一个文件路径数组filepath
filepath = []
suffix = '.csv'
# Files = 'SppedByHdfs/'
# 塞得港口泊位
Files = 'singaporePOICu/'

for parent, dirnames, filenames in os.walk(Files):
	for filename in filenames:
		# print(bohaiFiles + filename)
		# data = data.append(pd.read_csv(bohaiFiles + filename, header=None))
		filepath.append(Files + filename)
# print(len(filepath))
list1 = []
list2 = []
fileslen = len(filepath)
for i in range(fileslen):
	# print(filepath[i])
	out_df = pd.DataFrame()
	df = pd.read_csv(filepath[i], header=None)
	train_data = np.array(df)  # np.ndarray()
	train_x_list = train_data.tolist()  # list
	# print(train_x_list)
	# print(type(train_x_list))
	points = MultiPoint(train_x_list)
	# print(points.centroid.x)
	list1.append(points.centroid.x)
	list2.append(points.centroid.y)
print(len(list1))
print(len(list2))

# list 转变成DataFrame
df1 = pd.DataFrame(list1)
df2 = pd.DataFrame(list2)
print(df1.shape)

# 按列合并两个dataFrame ,并输出到文本文件中
out = pd.concat([df1, df2], axis=1)
print(out.shape)
out.to_csv('outPut/' + 'singaporePOICuzhongxindian', header=False, index=False)
