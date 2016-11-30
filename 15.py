# -*- coding: utf-8 -*-
# @Time     : 2016/11/18 11:15
# @Author   : Span
# @Site     : 
# @File     : 15.py
# @Function : http://www.pythonchallenge.com/pc/return/uzi.html
# @Software : PyCharm

## he ain't the youngest, he is the second
##todo: buy flowers for tomorrow
##tomorrow是1XX6年1月27日 并且是星期二 买花作甚呢
##图片的后面有12月份和2月份的日历，2月份有29天 是闰年 则这一年满足的条件有，今年是闰年，几年的1月27日是星期二
##这样的年份应该不止一个 根据提示 他不是最年轻的 是第二个年轻的

import  datetime

#先选出满足条件的所有
years = [y for y in range(1006,1997) if str(y)[-1]== '6' and y % 4 == 0]

year_c = []
for y in years:
    #根据具体的日期来确定候选年份
    d = datetime.date(y,1,27)
    if d.weekday() == 1:
        year_c.append(y)

#选出候选年份中的倒数第二个
print year_c[-2]  #mozart 1976 01 27 是mozart的诞辰