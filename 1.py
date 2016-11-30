# -*- coding: utf-8 -*-
# @Time     : 2016/9/10 18:19
# @Author   : Span
# @Site     : 
# @File     : 1.py
# @Function : http://www.pythonchallenge.com/pc/def/map.html
# @Software : PyCharm
#注意python2.x 和3.x中maketrans使用的不同之处
#http://www.jb51.net/article/63987.htm
import string
a = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
table = string.maketrans('abcdefghijklmnopqrstuvwxyz','cdefghijklmnopqrstuvwxyzab')
print a.translate(table)
print 'map'.translate(table)
