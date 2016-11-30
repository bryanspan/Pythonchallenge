# -*- coding: utf-8 -*-
# @Time     : 2016/11/18 13:40
# @Author   : Span
# @Site     : 
# @File     : 16.py
# @Function : http://www.pythonchallenge.com/pc/return/mozart.html
# @Software : PyCharm

from PIL import Image
import numpy as np

im = Image.open('mozart.gif')
# getdata() 返回一个图像内容的像素值序列。不过，这个返回值是 PIL 内部的数据类型，只支持确切的序列操作符，包括迭代器和基本序列方法。
imdata = list(im.getdata())   ##列表
imdata = np.array(imdata)  ## 数组
imdata = imdata.reshape((480,640))  ##改变数组的维度
imdata2 = np.zeros(imdata.shape)  ##初始化一个空的像素数组
print imdata2

for row in range(imdata.shape[0]):
    #紫色线段的坐标
    idx = np.where(imdata[row,:] == 195)
    #紫色的像素之前还有一个白色的像素
    idx = idx[0][0]-1
    # 循环平移，将紫色段移到每一行开头
    imdata2[row,:] = np.r_[imdata[row,idx : 640],imdata[row,0 : idx]]   #从定义的位置开始重新构造列表

imdata2.shape = (480 * 640,1)   ##转换为一个序列对象 因为putdata接受的参数要求为A sequence object.
print imdata2.shape
im.putdata(imdata2)
im.show() ## romance