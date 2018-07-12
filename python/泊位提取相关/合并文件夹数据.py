#-*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/5/30'
"""
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn import metrics
from sklearn.cluster import DBSCAN
import pandas as pd
from sklearn.preprocessing import StandardScaler
import os
import os.path


filepath = 'test9/'
data = pd.DataFrame()
for parent, dirnames, filenames in os.walk(filepath):
	for filename in filenames:
		f = filepath + filename
		print(f)
		data = data.append(pd.read_csv(filepath + filename, header=None))
data =data.iloc[:,10:]
print(data)
# data.to_csv('test9out/'+'polygon',index=False,header=False)
