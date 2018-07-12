# 去除文件夹中的轨迹点比较少的轨迹文件
import pandas as pd
import os.path

Files = []
data = pd.DataFrame()
# filepath = 'D:/航海项目/数据相关/泊位最新数据/singapore-indianIMO-678DATA/'
filepath = 'D:/北工大郑振涛/集群数据下载目录/6MonthBerthTraningDatatingliushichangFinal/'
# D:\航海项目\数据相关\100+v0.001+time600s
suffix = '.csv'
for parent, dirnames, filenames in os.walk(filepath):
	for filename in filenames:
		f = filepath + filename
		Files.append(filepath + filename)
		# print(filepath + filename)
		# print(f)
		# print(os.path.getsize(filepath+filename))
		# # 添加判断条件，如果文件大小为0的话则删除此文件,单位是b,去除小于5kb的文件
		# if(os.path.getsize(filepath+filename)==0.0):
		#     os.remove(filepath+filename)
# 如果轨迹点的数目小于300，则删除此mmsi文件.
fileslen = len(Files)
print(fileslen)
for i in range(fileslen):
	print(Files[i])
	# df = pd.read_csv(Files[i], header=None,error_bad_lines=False)
	df = pd.read_csv(Files[i], header=None, error_bad_lines=False)

	if (len(df) < 2):
		os.remove(Files[i])
