# -*- coding: utf-8 -*-
# @Time     : 2016/9/10 20:01
# @Author   : Span
# @Site     : 
# @File     : 2.txt.py
# @Function : http://www.pythonchallenge.com/pc/def/ocr.html
# @Software : PyCharm
# find rare characters in the mess 2.txt:

from itertools import permutations   #排列 combinations是组合
# filepath = './2.txt'
# file = open(filepath)
# a = ''                  #str
# b = []                  #list
# c = []
# for line in file.readlines():
#     a = list(line)      #将一行字符读取到一个列表中
#     b.extend(a)         #将所有的字符包括换行符都存入一个列表中
# myset = set(b)          #将列表中的元素进行去重
# for item in myset:     #准备筛选集合中的字符
#     print "the "+item+" has found "+str(b.count(item))+" times"   #b.count(item) 对集合中的每个元素进行计数
#     if b.count(item)==1:    #记录只出现了一次的字符
#         c.append(item)      #存入一个列表当中
# print ''.join(c)            #如果是单词 作为字符串出现更能让人接受
# ##  8!
# for a in  list(permutations(''.join(c),len(c))):    #列表中有8个字母 这8个字母可能组成的单词不止一个 所以对其进行排列
#         print ''.join(a)                            #结果将会有8！ = 40320 中可能的结果

import collections
data = ''.join([line.rstrip() for line in open('2.txt')])
OCCURRENCES = collections.OrderedDict()
for c in data:
    OCCURRENCES[c] = OCCURRENCES.get(c, 0) + 1
    avgOC = len(data) // len(OCCURRENCES)
    print ''.join([c for c in OCCURRENCES if OCCURRENCES[c] < avgOC])



