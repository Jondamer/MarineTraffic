#-*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/4/9'
"""
import pandas as pd
import os.path
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = 'NSimSun,Times New Roman'
# 加载数据
data = pd.read_csv('data/BerthSTtime', header=None)
AnchorData = pd.read_csv('6MonthAnchorTraningData4-4tingliushichang1-1-2-2/AnchorSTtime.csv', header=None)
print(data.head())
print(AnchorData.head())
#泊位训练集数据
x_up = data.loc[0:, 0:0].values
x_up_list = list(x_up)
y_up = data.loc[0:, 1:1].values
y_up_list = list(y_up)
# 锚地训练集数据坐标数据
x_down = AnchorData.loc[0:, 0:0].values
x_down_list = list(x_down)
y_down = AnchorData.loc[0:, 1:1].values
y_down_list = list(y_down)

plt.xlabel('x')
plt.ylabel('ST')
plt.title('Berth & Anchor StopTime Statics')
plt.scatter(x_up_list, y_up_list, c='red', alpha=1, marker='+', label='berth') # c='red'定义为红色，alpha是透明度，marker是画的样式
plt.scatter(x_down_list, y_down_list, c='blue', alpha=1, marker="+", label='Anchor') # c='blue'定义为蓝色
plt.grid(True)
plt.legend(loc='best')
plt.show()
