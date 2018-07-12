import pandas as pd
import time
import math as mt
import os
import os.path
# filepath = '../TankerShips/412203480-r-00001'
#定义一个文件路径数组filepath
filepath=[]
suffix = '.csv'
Files = 'D:/航海项目/数据相关/泊位最新数据/shanghai-hongkong - 副本/'
# Files = 'D:/航海项目/数据相关/泊位最新数据/02-IMOExtractByMMSI - 副本/'
# D:\航海项目\数据相关\泊位最新数据\02EXtIMO
# bohaiFiles = 'D:/航海项目/数据相关/泊位最新数据/02-IMOExtractByMMSI/'

# lllon=32.8373
# urlon=117.993
# lllat=-43.48
# urlat=30.2573

# lllon=76.5574
# urlon=105.667
# lllat=0.141336
# urlat=9.0854

# 上海 port - 香港 Port
lon1=121.571666
lon2=114.3333
lat1=31.412222
lat2=22.5

for parent, dirnames, filenames in os.walk(Files):
    for filename in filenames:
        # print(bohaiFiles + filename)
        # data = data.append(pd.read_csv(bohaiFiles + filename, header=None))
        #将文件的路径保存在filepath中
        filepath.append(Files + filename)
print(len(filepath))


df=pd.DataFrame()
fileslen=len(filepath)
for i in range(fileslen):
    print(filepath[i])
    out_df = pd.DataFrame()
    df = pd.read_csv(filepath[i], header=None,error_bad_lines=False)
    # df = pd.read_csv(filepath[i], header=None,skipinitialspace =True)
    df = df.sort_index()
    df = df.sort_values(by=0)
    print(df.shape)
    testlen = len(df)
    # print("--------------------")
    # print (testlen)
    for j in range(testlen):
        new_df = pd.DataFrame()
        # print(abs(df.iloc[j,1]-lon1) )
        # print('纬度的插值是：')
        # print(abs(df.iloc[j, 2] - lat1))
        # 选择地方是出发港，所以出发的时间要保持在前面
        if ( abs(df.iloc[j,1]-lon1)<1 and  abs(df.iloc[j,2]-lat1)<1 ) :
            print(abs(df.iloc[j,1]-lon1))
            if(j<100):
                out_df = out_df.append(df)
                print('****************************')
                print(out_df.shape)
            break
    for k in range(testlen):
        if (abs(df.iloc[k,1]-lon2)<1 and abs(df.iloc[k,2]- lat2)<1):
            print('+++++++++++++++++++++++++++++++')
            out_df.to_csv('D:/航海项目/数据相关/泊位最新数据/shanghai-hongkong/' + filepath[i].split('/')[5][0:9], index=False, header=False)
            break