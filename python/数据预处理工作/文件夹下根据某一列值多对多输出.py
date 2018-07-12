
import pandas as pd
import time
import math as mt
import os
import os.path

# filepath = '../TankerShips/412203480-r-00001'
# 定义一个文件路径数组filepath
filepath = []
suffix = '.csv'
# Files = 'SppedByHdfs/'
Files = 'SpeedByCal/'


for parent, dirnames, filenames in os.walk(Files):
    for filename in filenames:
        # print(bohaiFiles + filename)
        # data = data.append(pd.read_csv(bohaiFiles + filename, header=None))
        filepath.append(Files + filename)
print(len(filepath))

fileslen = len(filepath)
for i in range(fileslen):
    print(filepath[i])
    out_df = pd.DataFrame()
    df = pd.read_csv(filepath[i], header=None)
    # df = pd.read_csv(filepath[i], header=None,error_bad_lines=False)
    # df = pd.read_csv(filepath[i], header=None,skipinitialspace =True)
    # df = df.iloc[:, 0:8]
    # df = df.sort_index()
    # df = df.sort_values(by=0)
    print(df.shape)
    testlen = len(df)
    # print("--------------------")
    print(testlen)
    k = 0
    for j in range(testlen-1):
        if (df.iloc[j, 5] == df.iloc[j + 1, 5]):
            new_df = pd.DataFrame()
            new_df.insert(0, '0', [df.iloc[j, 0]])
            new_df.insert(1, '1', [df.iloc[j, 1]])
            new_df.insert(2, '2', [df.iloc[j, 2]])
            new_df.insert(3, '3', [df.iloc[j, 3]])
            new_df.insert(4, '4', [df.iloc[j, 4]])
            new_df.insert(5, '5', [df.iloc[j, 5]])
            out_df = out_df.append(new_df)
        else:
            out_df.to_csv('SpeedByCalOut/'+ filepath[i].split('/')[1][0:10]+"-"+ str(k), index=False, header=False)
            k = k + 1
            out_df = pd.DataFrame()
    continue
