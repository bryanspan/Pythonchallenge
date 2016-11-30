# -*- coding: utf-8 -*-
# @Time     : 2016/11/12 21:47
# @Author   : Span
# @Site     : 
# @File     : 11.py
# @Function : http://www.pythonchallenge.com/pc/return/5808.html
# @Software : PyCharm

#查看源码：title为 odd even
from PIL import Image
img = Image.open("cave.jpg")
# img = Image.open("evil1.jpg")
# print img.size
# print img.getpixel((0,0))
# print img.getpixel((0,1))
# print img.getpixel((0,2))
# print img.getpixel((1,0))
# print img.getpixel((639,479))
w,h = img.size
for i in range(w):
    for j in range(h):
        if (i + j)%2 == 1:
            img.putpixel((i,j),0)
img.save('cave2.jpg')   # evil
img.show()