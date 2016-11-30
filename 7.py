# -*- coding: utf-8 -*-
# @Time     : 2016/11/1 22:02
# @Author   : Span
# @Site     : 
# @File     : 7.py
# @Function : http://www.pythonchallenge.com/pc/def/oxygen.html
# @Software : PyCharm

##观察图片： 一个灰度图像块占用7*9个像素，总长度为608(实应为609 第一个灰度图像块少了两个像素)所以总的灰度块有87个
##L模式的图像getdata之后只包含一个值 将每一个值与ascII码对应 得到灰度块所表示的信息
##一个灰度块表示一个字符的ascii码 但是一个灰度块占用7个像素 所以中间转换的时候取步长为7

#导入图片处理包
from PIL import Image


#打开图片
img =  Image.open("oxygen.png")

#先把oxygen.png上的灰色区域切割下来
#根据在GIMP中对图片的分析 裁剪的区域像素为
#参数：left，top，right，bottom
area = (0,43,608,52)

#裁剪
cut = img.crop(area)

#
pixels = cut.getdata()

print type(pixels)
print "mode: %s \n amount od pixel: %d" % (cut.mode,len(pixels))
print pixels[0]  ##RGBA 四个值

#转化为L模式(黑白模式)
lcut = cut.convert('L')
lpixels = lcut.getdata()
print "mode: %s \n amount od pixel: %d" % (lcut.mode,len(lpixels))
print lpixels[0]  ##只有一个值

str = []
for i in range(0,608,7):  ##7个像素 表示的是一个字符的ascii码
    str.append(chr(lpixels[i]))
    print i
print ''.join(str)
##输出结果为：smart guy, you made it. the next level is [105, 110, 116, 101, 103, 114, 105, 116, 121]
print len(str)
##输出结果：87

result = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print ''.join(chr(x) for x in result)
##输出结果为：integrity