# -*- coding:utf-8 -*-
from sklearn import tree
import pandas as pd
import os
import time
import numpy as np
from sklearn.ensemble import RandomForestClassifier

#
# 从外部读取训练数据集，训练算法模型
TD = pd.DataFrame()
TD.data = pd.DataFrame()
TD.target = pd.DataFrame()
TD = pd.read_csv('TrainingData/TR.txt', header=None)
TD.dropna(inplace=True)
TD.columns = ['stopTime', 'Dis Variance', 'Velocity Mean', 'Velocity Variance',
			  'Dis mean', 'a -mean', 'a Variance', 'L_F Point Dis', 'maxDis', 'TT', 'Density', 'Class label']
TD.info()
TD.data = TD.iloc[:, 0:11]
TD.target = TD.iloc[:, 11:12]
print(TD.target.head(2))
TD.target = np.ravel(TD.target)
print(TD.data.head(10))
# print (TD.target.head(10))
# print ('\n')
forest = RandomForestClassifier(n_estimators=100, random_state=0, n_jobs=-1)
# np.ravel().forest.fit(TD.data, TD.target)
# 计算模型训练的时间
start = time.clock()
forest.fit(TD.data, TD.target)
elapsed = (time.clock() - start)
print(elapsed)
print('Model Training Finished！')
#
# # 评估特征的重要性
# # feat_labels = TD.columns[0:9]
# # importances = forest.feature_importances_
# # indices = np.argsort(importances)[::-1]
# # print (TD.data.shape)
# #
# # for f in range(TD.data.shape[1]):
# #     print("%2d) %-*s %f" % (f + 1, 30, feat_labels[f], importances[indices[f]]))
#
filepath = []
# 从外部读取实际数据,外部数据以文件夹的形式进行保存,并将分类结果输出到文本文件中
Files = 'DataInput/'
for parent, dirnames, filenames in os.walk(Files):
	for filename in filenames:
		filepath.append(Files + filename)
fileslen = len(filepath)
Data = pd.DataFrame()
FeaturesData = pd.DataFrame()
for i in range(fileslen):
	print(filepath[i])
	out_df = pd.DataFrame()
	out_dfs = pd.DataFrame()
	df = pd.read_csv(filepath[i], header=None)
	testlen = len(df)
	# print("--------------------")
	# print (testlen)
	Data = df.iloc[:, 0:6]
	FeaturesData = df.iloc[:, 5:]
	# print 'FeaturesData记录数'
	# print len(FeaturesData)
	# print FeaturesData.head(1)
	ll = forest.predict(FeaturesData)
	# print ll
	# print '\n'
	# print type(ll)
	# numpy.ndarray 数据类型转变成dataFrame 数据类型
	biaoqian = pd.DataFrame(ll)

	# print 'll 的数据类型：'
	# print type(biaoqian)
	# print biaoqian.shape

	# 按列合并两个dataFrame
	lls = pd.DataFrame()
	lls = pd.concat([Data, biaoqian], axis=1)

	# lls = pd.concat([FeaturesData, biaoqian], axis=1)
	# print lls.shape
	# print type(lls)
	# 输出到文本文件
	# 重置索引
	# lls=lls.reset_index(drop=True)
	# lls.to_csv('DataOut2/' + 'out2', index=False, header=False)
	lls.columns = ['timeStamp', 'mmsi', 'lon ', 'lat', 'velocity', 'ST', 'Classlabel']
	lls1 = lls[lls.Classlabel == 0]
# print df1
	lls1.to_csv('BerthData/' + filepath[i].split('/')[1][0:], index=False, header=False)
# lls1.to_csv('BerthData/' + 'berthData', index=False, header=False)
	lls2 = lls[lls.Classlabel == 1]
# print df2
	lls2.to_csv('AnchorData/' + filepath[i].split('/')[1][0:], index=False,header=False)