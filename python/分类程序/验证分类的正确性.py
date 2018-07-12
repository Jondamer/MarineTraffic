# -*- coding:utf-8 -*-
from __future__ import division
import pandas as pd
import time
import math as mt
import os
import os.path

filepath1 = []
filepath2 = []
Files1 = 'DataInput2/'
Files2 = 'DataOut2/'
# bohaiFiles = 'D:/航海项目/412415680-r-00000'
for parent, dirnames, filenames in os.walk(Files1):
	for filename in filenames:
		filepath1.append(Files1 + filename)

for parent, dirnames, filenames in os.walk(Files2):
	for filename in filenames:
		filepath2.append(Files2 + filename)

fileslen = len(filepath1)
for i in range(fileslen):
	print(filepath1[i])
	out_df = pd.DataFrame()
	out_dfs = pd.DataFrame()
	df1 = pd.read_csv(filepath1[i], header=None)
	df2 = pd.read_csv(filepath2[i], header=None)
	testlen = len(df1)
	i = 0
	for j in range(testlen - 1):
		if (df1.iloc[j, 11] == df2.iloc[j, 9] and df1.iloc[j,11]==0):
			i = i + 1
	print (i)
	print (testlen)
	percent = (i / 1397)
	print('泊位分类的正确率是：')
	print (percent)

	k = 0
	for j in range(testlen - 1):
		if (df1.iloc[j, 11] == df2.iloc[j, 9] and df1.iloc[j,11]==1):
			k = k + 1
	print (k)

	percent1 = (k / 3293)
	print('锚地分类的正确率是：')
	print(percent1)
