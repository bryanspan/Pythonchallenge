# -*- coding: utf-8 -*-
# @Time     : 2016/11/13 21:42
# @Author   : Span
# @Site     : 
# @File     : 12.py
# @Function : http://www.pythonchallenge.com/pc/return/evil.html
# @Software : PyCharm
##title name dealling evil
##查看evil1.jpg的像素特征 并没有找出来什么有规律的线索
##因为有evil1 所以试试evil2.jpg 看到有新的线索
##但是gfx是什么东西不知道 用UE打开  一堆二进制数据 看不懂  详见 https://www.cs.duke.edu/courses/cps124/fall01/code/gfx_reader/docs/gfx_format.html
##从12关的图片上看到一个人在分发五份牌 so将原来的gtx文件字节也分为五份


# data = open("evil2.gfx", "rb").read()
# print len(data)
# for i in range(5):
#     open("%d.jpg" % i,"wb").write(data[i::5])       ##输出五张图片 分别是dis pro port ional
# # print data

##同样的方法
with open('evil2.gfx', 'rb') as inFile:
    data = inFile.read()

for i in range(5):
    with open('%d.jpg' % i, 'wb') as outFile:
        outFile.write(data[i::5])