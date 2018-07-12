import pandas as pd
import time
import math as mt
import os
import os.path

# filepath = '../TankerShips/412203480-r-00001'
# 定义一个文件路径数组filepath
filepath = []
suffix = '.csv'
# bohaiFiles = 'D:/航海项目/数据相关/泊位最新数据/IMOExtractByMMSI/'D:\航海项目\数据相关\泊位最新数据\678POI\POI1
bohaiFiles = 'D:/zzt/0001/'
for parent, dirnames, filenames in os.walk(bohaiFiles):
	for filename in filenames:
		# print(bohaiFiles + filename)
		# data = data.append(pd.read_csv(bohaiFiles + filename, header=None))
		# 将文件的路径保存在filepath中
		filepath.append(bohaiFiles + filename)
print(len(filepath))

fileslen = len(filepath)
for i in range(fileslen):
	print(filepath[i])
	# 应对有些文件存在格式不对，解决部分属性列缺失报错的问题。
	# df = pd.read_csv(filepath[i], header=None,error_bad_lines=False)
	df = pd.read_csv(filepath[i], header=None)
	df = df.sort_index()
	df = df.sort_values(by=0)
	df.columns = ['utc', 'mmsi', 'status','lon', 'lat', 'cog', 'head']
	df = df[df.status == 1]
	df = df.drop_duplicates()
	# df = df[df.iloc[]]
	df.to_csv('D:/zzt/0001/' + filepath[i].split('/')[3][0:8] + suffix, index=False, header=False)
