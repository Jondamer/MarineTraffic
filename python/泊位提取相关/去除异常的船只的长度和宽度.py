# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/7/5'
"""
import pandas as pd

df = pd.read_csv('Polygon/port1lenwidhead', header=None)
# 遍历船只长度列的最大值和最小值
# print(df.head(10))
df.columns = ['lon', 'lat', 'head', 'length', 'width']
print(df.length.max())
# print(df[df.length > 500])

# print(df.length.max())

lens = len(df)
for i in range(lens):
	# print(type(df.iloc[i, 3]))
	if ((df.iloc[i, 3]) > 500):
		df.iloc[i:i + 1, 3:4] = 500
	if(df.iloc[i, 3]/df.iloc[i, 4]>10 and df.iloc[i, 3]/df.iloc[i, 4]<20):
		print(df.iloc[i, 3],df.iloc[i, 4])
# print(df.length.max())
# output
# df.to_csv('port1lenwidhead7-5', header=None, index=None)
