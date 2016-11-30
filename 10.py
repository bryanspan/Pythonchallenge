# -*- coding: utf-8 -*-
# @Time     : 2016/11/5 16:21
# @Author   : Span
# @Site     : 
# @File     : 10.py
# @Function : http://www.pythonchallenge.com/pc/return/bull.html
# @Software : PyCharm
# a = [1, 11, 21, 1211, 111221,
# look and say sequence 看读序列
# 后一个数字为前一个数字读出的结果
#初始为1，后一个为1个1，就是11，后一个为2个1 就是21， next就是1个2，1个1就是1211 以此类推
#https://oeis.org/A005150
def look_and_say(member):
    while True:
        yield member
        breakpoints = ([0] + [i for i in range(1, len(member)) if member[i - 1] != member[i]]  #区分不同的数字作为断点 构造出一个列表
                       + [len(member)])                                                         #两个断点确定一个数字的数目
        print 'breakpoints:',breakpoints
        groups = [member[breakpoints[i - 1]:breakpoints[i]] for i in range(1, len(breakpoints))]
        print 'groups:', groups                             #根据breakpoints将member分组 相同的数字属于一个group
        member = ''.join(str(len(group)) + group[0] for group in groups)

# Print the 30-element sequence beginning with "1"
sequence = look_and_say("1")
for i in range(10):# 30
    print next(sequence) #python2应为print sequence.next()
print len(next(sequence))  #5808