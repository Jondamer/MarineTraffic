# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/7/6'
"""
import pandas as pd

data = pd.DataFrame()
data = pd.read_csv('fullYearAllships20bitsGrid', header=None, sep=',')
data.columns = ['lon', 'lat', 'num']
print(data.head(10))
data = data[data['num'] >30]
# # print(data)
data = data.iloc[:,0:2]
data.to_csv('inData/'+'fullYearAllships20bitsGridby30', header=None, index=None)
