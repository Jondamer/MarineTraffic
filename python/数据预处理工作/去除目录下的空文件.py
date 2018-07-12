#去除文件夹中的空文件
import pandas as pd
import os.path
data = pd.DataFrame()
# filepath = 'D:/航海项目/数据相关/泊位最新数据/678POI/POI4/'
filepath = 'D:/zzt/4-28/BerthData/'
# filepath = 'D:/航海项目/数据相关/泊位最新数据/shanghai-hongkong/'
# D:\航海项目\数据相关\100+v0.001+time600s
suffix = '.csv'
for parent, dirnames, filenames in os.walk(filepath):
    for filename in filenames:
        f=filepath+filename
        print(filepath + filename)
        print(f)
        print(os.path.getsize(filepath+filename))
        # 添加判断条件，如果文件大小为0的话则删除此文件,单位是b,去除小于5kb的文件
        if(os.path.getsize(filepath+filename)==0.0):
            os.remove(filepath+filename)
