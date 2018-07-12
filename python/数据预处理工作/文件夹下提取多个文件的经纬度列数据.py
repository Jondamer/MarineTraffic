import pandas as pd
import time
import math as mt
import os
import os.path
# filepath = '../TankerShips/412203480-r-00001'
#定义一个文件路径数组filepath
filepath=[]
suffix = '.csv'
Files = 'D:/航海项目/数据相关/泊位最新数据/Test/'
# bohaiFiles = 'D:/航海项目/数据相关/泊位最新数据/02-IMOExtractByMMSI/'
for parent, dirnames, filenames in os.walk(Files):
    for filename in filenames:
        # print(bohaiFiles + filename)
        # data = data.append(pd.read_csv(bohaiFiles + filename, header=None))
        #将文件的路径保存在filepath中
        filepath.append(Files + filename)
print(len(filepath))



fileslen=len(filepath)
for i in range(fileslen):
    print(filepath[i])
    out_df = pd.DataFrame()
    df = pd.read_csv(filepath[i], header=None)
    # df = pd.read_csv(filepath[i], header=None,error_bad_lines=False)
    # df = pd.read_csv(filepath[i], header=None,skipinitialspace =True)
    # df = df.iloc[:, 0:8]
    df = df.sort_index()
    df = df.sort_values(by=0)
    print(df.shape)
    testlen = len(df)
    # print("--------------------")
    print (testlen)
    for j in range(testlen):
     # if(len(df.iloc[j])>2):
     #    print(df.iloc[j].size)
        new_df = pd.DataFrame()
        new_df.insert(0, '0', [df.iloc[j, 0]])
        new_df.insert(1, '1', [df.iloc[j, 6]])
        new_df.insert(2, '2', [df.iloc[j, 7]])
        new_df.insert(3, '3', [df.iloc[j, 25]])
        out_df = out_df.append(new_df)
    out_df.to_csv('D:/航海项目/数据相关/泊位最新数据/TestOut/' + filepath[i].split('/')[5][0:9] , index=False, header=False)
