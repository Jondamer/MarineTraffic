import pandas as pd
import time
import math as mt
import os
import os.path

# filepath = '../TankerShips/412203480-r-00001'
# 定义一个文件路径数组filepath
filepath = []
suffix = '.csv'
bohaiFiles = 'D:/zzt/BerthData/in/'

for parent, dirnames, filenames in os.walk(bohaiFiles):
	for filename in filenames:
		# print(bohaiFiles + filename)
		# data = data.append(pd.read_csv(bohaiFiles + filename, header=None))
		# 将文件的路径保存在filepath中
		filepath.append(bohaiFiles + filename)
print(len(filepath))

df = pd.DataFrame()
fileslen = len(filepath)
for i in range(fileslen):
	print(filepath[i])
	out_df = pd.DataFrame()
	df = pd.read_csv(filepath[i], header=None, error_bad_lines=False)
	out_df = df.iloc[:, 5:]
	print(out_df.shape)
	testlen = len(out_df)
	out_df.to_csv('D:/zzt/BerthData/out/' + filepath[i].split('/')[4][:30] + suffix, index=False, header=False)
