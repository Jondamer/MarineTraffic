# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/7/6'
"""
import pandas as pd

data = pd.DataFrame()
data = pd.read_csv('bohaiwanxibo7-8-9monthPOI18bits', header=None, sep=',')
data.columns = ['lon', 'lat', 'num']
print(data.head(10))
data = data[data['num'] >0]
# # print(data)
data = data.iloc[:,0:2]
data.to_csv('inData/'+'bohaiwanxibo7-8-9monthPOI18bitsby0', header=None, index=None)
