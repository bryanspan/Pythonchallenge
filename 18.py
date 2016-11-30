# -*- coding: utf-8 -*-
# @Time     : 2016/11/20 15:20
# @Author   : Span
# @Site     : 
# @File     : 18.py
# @Function : http://www.pythonchallenge.com/pc/return/balloons.html
# @Software : PyCharm
# @Solution : http://kwangka.github.io/2015/02/01/pc18/

# from PIL import Image
##将两张图片的亮度值相减putpixel到一张图片中看结果
# img = Image.open("balloons.jpg")
# im1 = img.convert("YCbCr")
# newIm = Image.new(img.mode,(375,335))
# for i in range(375):
#     for j in range(335):
#         newIm.putpixel((i,j),im1.getpixel((i+374,j))[0]-im1.getpixel((i,j))[0])
# newIm.show()  ##结果并没有什么有用的信息 尝试失败 考虑的太复杂  it is more obvious that what you might think
# 参照solution 亮度 brightness 更换为链接 进入页面图片没有发生变化 但是源码中的提示 maybe consider deltas.gz
# 继续更改链接 下载deltas.gz到本地 打开查看其中的txt  包含两列 很明显要作比较
import gzip
import codecs
import difflib
import re
f = gzip.open('deltas.gz','rb')
contents = f.read()
f.close()

lines = contents.strip().split('\n')  ##将文件中的数据按行存储到列表lines中 再按行处理 前一部分放进str1中 后一部分放入str2中

str1 = []
str2 = []
for line in lines:
    str1.append(line[0:53])
    str2.append(line[56:109])

##https://docs.python.org/2/library/difflib.html
str_diff = list(difflib.Differ().compare(str1,str2))   ##'-'表示字符只存在于str1中 '+'表示字符只存在与str2中 ' '表示字符在str1和str2中都存在
print str_diff
png_datas = [''.join(filter(lambda l : l[0] == c, str_diff)) for c in ' -+']
# print png_datas
for i in range(len(png_datas)):
    png_data = re.sub(r'[^0-9a-fA-F]','',png_datas[i])
    png_data = codecs.getdecoder('hex')(png_data)[0]
    with open(('png%d'% i),'wb') as handle:
        handle.write(png_data)

##../hex/bin.html
##UN:butter
##PWD:fly