# -*- coding: utf-8 -*-
# @Time     : 2016/9/13 9:51
# @Author   : Span
# @Site     : 
# @File     : 5.py
# @Function : http://www.pythonchallenge.com/pc/def/peak.html
# @Software : PyCharm
# @Solution :

import urllib2

#对象序列化以及反序列化dumps() 和 load()
import cPickle as pickle

# 美观打印的结果 such as 用print 输出的是一行数据 但是数据是存在一定结构的 此时用pprint就可以输出多行 更清楚的发现数据的特征
# 作用就是更加美观的打印出数据结构
import pprint

f=urllib2.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
print type(f)
# Create an unpickler 并且.load()是通过这个文件来unpickler这个对象
result=pickle.Unpickler(f).load()

pprint.pprint(result)

output = open('5.txt', 'w')
for line in result:
    print ''.join([c[0]*c[1] for c in line])
output.close()