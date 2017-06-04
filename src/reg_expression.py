# -*- coding: utf-8 -*-
"""
Created on Fri Jul 08 17:25:21 2016

@author: yumkong
"""
# import python regular expression module
import re
#match()方法判断是否匹配，如果匹配成功，返回一个Match对象，否则返回None

#test = 'abc-111666'
#if re.match(r'^\w{3}\-\d{3,8}$', test):
#    print 'ok'
#else:
#    print 'failed'
#
##can match a string composing of at least 1 space or 1 character
#re.split(r'[\s\,]+', 'a,b, c  d')
#
##extract hour minites and seconds using group ()
#t = '19:05:30'
#m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:\
#(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:\
#(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
#m.groups()
##****经过自已实验，也可以用以下更简便的写法：
#m1 = re.match(r'^([0-1]?[0-9]|2[0-3])\:([0-5]?[0-9])\:([0-5]?[0-9])', t)
#m1.groups()

#prac1: 验证出类似的Email：
#someone@gmail.com
#bill.gates@microsoft.com
re_email_whole = re.compile(r'[\w\.]+@\w+\.\w+')
test_email = 'yuguang.liu@gmail.com'
if re_email_whole.match(test_email):
    print 'Valid email address'
else:
    print 'Invalid email address'
re_email_group = re.compile(r'([\w\.]+)@(\w+)\.(\w+)')
re_email_group.match('yuguang.liu@gmail.com').groups()

#prac2: 验证并提取出带名字的Email地址：
#<Tom Paris> tom@voyager.org
re_name_email = re.compile(r'^(\<[\w\s]+\>)\s+([\w\.]+@\w+\.\w+)')
t_email = '<Tom Paris> tom@voyager.org'
matchres = re_name_email.match(t_email)
if matchres:
    print 'Valid email address'
    names = matchres.groups()
    if len(names) > 1:
        print 'name is: ' + names[0][1:-1]
else:
    print 'Invalid email address'
