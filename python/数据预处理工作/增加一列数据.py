#-*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/5/8'
"""

import pandas as pd
import time
import math as mt
import os
import os.path


filepath='AnchorTraining9Features/'

outpath='out'
df = pd.DataFrame()
df = pd.read_csv(filepath,header=None)
# df[:,:9]=1
# 增加索引列
df.to_csv(outpath,header=None,index=True)