import pandas as pd
import time
import math as mt
import os
import os.path
# filepath = '../TankerShips/412203480-r-00001'
#定义一个文件路径数组filepath
filepath=[]
suffix = '.csv'
bohaiFiles = 'D:/航海项目/数据相关/泊位最新数据/马六甲-印度区域/'
# D:\航海项目\数据相关\泊位最新数据\02EXtIMO
# bohaiFiles = 'D:/航海项目/数据相关/泊位最新数据/02-IMOExtractByMMSI/'

# lllon=32.8373
# urlon=117.993
# lllat=-43.48
# urlat=30.2573

lllon=76.5574
urlon=105.667
lllat=0.141336
urlat=9.0854

for parent, dirnames, filenames in os.walk(bohaiFiles):
    for filename in filenames:
        # print(bohaiFiles + filename)
        # data = data.append(pd.read_csv(bohaiFiles + filename, header=None))
        #将文件的路径保存在filepath中
        filepath.append(bohaiFiles + filename)
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
        if ( lllon <df.iloc[j,1]  and df.iloc[j,1]<urlon  and  lllat <df.iloc[j,2]  and df.iloc[j,2]< urlat  ):
            new_df.insert(0, '0', [df.iloc[j, 0]])
            new_df.insert(1, '1', [df.iloc[j, 1]])
            new_df.insert(2, '2', [df.iloc[j, 2]])
            out_df = out_df.append(new_df)
    out_df.to_csv('D:/航海项目/数据相关/泊位最新数据/新加坡-斯里兰卡/' + filepath[i].split('/')[5][:30] + suffix, index=False, header=False)