# -*- coding: utf-8 -*-
# @Time     : 2016/9/11 1:20
# @Author   : Span
# @Site     : 
# @File     : 3.py
# @Function : http://www.pythonchallenge.com/pc/def/equality.html
# @Software : PyCharm
import re


a = []
data = ''.join([line.rstrip() for line in open('3.txt')])
pattern = re.compile(r'([^A-Z][A-Z]{3})([a-z]{1})([A-Z]{3}[^A-Z])') #使用分组的正则表达式去匹配
lowcaseletter = pattern.findall(data)   #获得已经分组的匹配结果
for i in lowcaseletter:                #找到我们需要的字段
    a.append(i[1])
print ''.join(a)
#linkedlilst