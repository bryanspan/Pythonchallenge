# -*- coding: utf-8 -*-
# @Time     : 2016/11/1 16:47
# @Author   : Span
# @Site     : 
# @File     : 6.py
# @Function : http://www.pythonchallenge.com/pc/def/channel.html
# @Software : PyCharm
import os
import re
import zipfile

# os.walk('路径名称') 返回包含三个字段的‘generator’类型
# 第一个字段表示的是当前的路径名称，
# 第二个字段表示当前路径下的子文件名，
# 第三个字段表示该目录下的文件的一个列表
list = os.walk("channel/")

filenum = 0
# 统计channel目录之下有多少文件
for root,dirs,file in list:     #获取三个字段的值 提取出文件的数目
    for f in file:
        filenum+=1
        print filenum

# 根据readme中的提示从90052开始阅读文件
startnum="90052"

for i in range(filenum):
    f = open("channel/"+startnum+".txt","r")
    content = f.read()
    p = re.compile(r'(\d+)')
    start = p.findall(content)          #返回一个列表
    # startnum = start[0]
    # print startnum
    for i in start:
        startnum = i
        print startnum


#创建一个ZipFile对象zf 表示一个zip文件
zf = zipfile.ZipFile("channel.zip")
id = "90052"
out = ""
while 1:
    text = zf.read("%s.txt" % id)       #读取zip文件内指定文件的二进制数据
    match = re.compile("Next nothing is (\d*)").search(text)
    if match:
        out += zf.getinfo("%s.txt" % id).comment         # zf.getinfo("%s.txt" % id) 获取一个ZipInfo对象，表示zip文档中相应文件的信息
        id = match.group(1)
    else:
        break
print out