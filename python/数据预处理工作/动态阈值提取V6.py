import pandas as pd
import os
import numpy as np
import os.path
m=20
n=40
# 稀疏度值s
S=0
countmax=0
# 断点区域经纬度
lllon1=120.712
urlon2=122.605
lllat1=35.9773
urlat2=36.9171

inputPath = 'D:/航海项目/数据相关/0001插值后的数据/'
outputPath='D:/航海项目/数据相关/001动态阈值结果/'

if __name__ == '__main__':
    out_df = pd.DataFrame()
    for (path,dirs,files) in os.walk(inputPath):
        for filename in files:
            out_df = out_df.append(pd.read_csv(inputPath+filename,header=None))

    testlen=len(out_df)
    out_new_df1 = pd.DataFrame()
    out_new_df2 = pd.DataFrame()
    for i in range(testlen):
      num=out_df.iloc[i,2]
      # print(out_df.iloc[i,0])
      if ( (out_df.iloc[i, 0] > lllon1) and (out_df.iloc[i, 0] < urlon2) and (out_df.iloc[i, 1]) > lllat1 and (out_df.iloc[i, 1] < urlat2) and  (out_df.iloc[
          i, 2]) > m):
          new_df = pd.DataFrame()
          print(out_df.iloc[i, 0], out_df.iloc[i, 1],out_df.iloc[i, 2])
          new_df.insert(0, '0', [out_df.iloc[i, 0]])
          new_df.insert(1, '1', [out_df.iloc[i, 1]])
          new_df.insert(2, '2', [out_df.iloc[i, 2]])
          out_new_df1 = out_new_df1.append(new_df)
          print(out_new_df1.shape)
      else:
          if (num > n):
              new_df = pd.DataFrame()
              print(out_df.iloc[i, 0], out_df.iloc[i, 1],out_df.iloc[i,2])
              new_df.insert(0, '0', [out_df.iloc[i, 0]])
              new_df.insert(0, '1', [out_df.iloc[i, 1]])
              new_df.insert(0, '2', [out_df.iloc[i, 2]])
              out_new_df2 = out_new_df2.append(new_df)

    frames=[out_new_df1,out_new_df2]
    result = pd.concat(frames, axis=0, ignore_index=True)

    print(result.shape)
    result.to_csv(outputPath + 'outdata20', index=False, header=False)
