# -*- coding: utf-8 -*-
# @Time     : 2016/11/3 16:37
# @Author   : Span
# @Site     : 
# @File     : 8.py
# @Function : http://www.pythonchallenge.com/pc/def/integrity.html
# @Software : PyCharm

#使用bz2压缩模块 不查不知道
import bz2
un = "BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084"
pw = "BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08"
username = bz2.decompress(un)
password = bz2.decompress(pw)
print username,password
##输出：huge file
