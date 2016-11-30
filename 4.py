# -*- coding: utf-8 -*-
# @Time     : 2016/9/12 1:32
# @Author   : Span
# @Site     : 
# @File     : 4.py
# @Function : http://www.pythonchallenge.com/pc/def/linkedlist.php
# @Software : PyCharm
import re, urllib,requests
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php"
newurl = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
htmlSource = urllib.urlopen(url).read()
linksList = re.findall('(\?.*)"><',htmlSource)
for i in range (400):
    url = newurl +str(linksList[0])
    htmlSource = requests.get(url).content
    linksList = re.findall('is(.*[0-9]*)',htmlSource)
    print i
    print url
#http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing= 66831
#SOLUTION:http://wiki.pythonchallenge.com/index.php?title=Level4:Main_Page


