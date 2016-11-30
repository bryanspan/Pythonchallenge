# -*- coding: utf-8 -*-
# @Time     : 2016/11/14 14:08
# @Author   : Span
# @Site     : 
# @File     : 13.py
# @Function : http://www.pythonchallenge.com/pc/return/disproportional.html
# @Software : PyCharm
#提示说phone that evil
#要用到xmlrpclib https://docs.python.org/2/library/xmlrpclib.html
#evil4页面有一张图片未显示出来 使用chrome打不开 更换浏览器 用IE打开之后提示 Bert is evil
import xmlrpclib
proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print proxy.system.listMethods()
print proxy.system.methodHelp('phone')
print proxy.phone('Bert')  #555-ITALY  链接ITALY提示SMALL LETTER italy进入下一关卡