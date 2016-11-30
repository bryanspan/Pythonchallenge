# -*- coding: utf-8 -*-
# @Time     : 2016/11/18 15:33
# @Author   : Span
# @Site     : 
# @File     : 17.py
# @Function : http://www.pythonchallenge.com/pc/return/romance.html
# @Software : PyCharm
# @Soulution: http://kwangka.github.io/2015/01/31/pc17/
from urllib2 import Request,build_opener,HTTPCookieProcessor,HTTPHandler
import urllib
import cookielib
import re
import bz2
import xmlrpclib

##本关的图片左下角是第四关的图片 图片名为cookies  线索 第四关 cookies
##声明一个CookieJar对象实例来保存Cookie
cj = cookielib.CookieJar()
##创建一个opener
# hander = HTTPCookieProcessor(cj)
# opener = build_opener(hander)
##创建一个opener实例
opener = build_opener(HTTPCookieProcessor(cj),HTTPHandler)
f = opener.open("http://www.pythonchallenge.com/pc/def/linkedlist.php")
# html = f.read()
# for cookie in cj:
#     print cookie
##创建一个Pattern 编译好的正则表达式
pat = re.compile('and the next busynothing is (\d+)')  ##（）表示一个分组 为之后的匹配提供索引
##r开头的字符串都是raw字符串 所有的字符串都不会被转义e.r'\n' 不会被认为是换行
url_template = r'http://www.pythonchallenge.com/pc/def/linkedlist.php?busynothing={0}'  ##{0}处待替换的数据
next_num = '12345'
cookies =[]
while True:
    f = opener.open(url_template.format(next_num))
    html = f.read()
    for cookie in cj:
        cookies.append(cookie)
        # print cookie
    matchRes = pat.findall(html)
    if matchRes:
        next_num = matchRes[0]
        print next_num
    else:
        break
print len(cookies)
print type(cookies[0])
values = [x.value for x in cookies]
msg = urllib.unquote_plus("".join(values))
print bz2.decompress(msg)

proxy = xmlrpclib.ServerProxy("http://www.pythonchallenge.com/pc/phonebook.php")
print proxy.phone("Leopold")

list(cj)[0].value = 'the+flowers+are+on+their+way'
print opener.open('http://www.pythonchallenge.com/pc/stuff/violin.php').read()