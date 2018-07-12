# -*- coding:utf-8 -*-
"""
__title__ = ''
__author__ = 'Administrator'
__time__ = '2018/6/5'
"""
# -*- coding: utf-8 -*-
'''
只使用与较小的文件，比较大的文件运行时间长
'''


def quchong(infile, outfile):
	infopen = open(infile, 'r', encoding='utf-8')
	outopen = open(outfile, 'w', encoding='utf-8')
	lines = infopen.readlines()
	list_1 = []
	for line in lines:
		if line not in list_1:
			list_1.append(line)
			outopen.write(line)
	infopen.close()
	outopen.close()


quchong("源文件路径", "目标文件路径")
