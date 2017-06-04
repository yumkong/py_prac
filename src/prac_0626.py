# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 20:42:14 2016

@author: yumkong
"""
# ***1-filter function***

def is_odd(n):
    return n % 2 == 1
#filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15])

#把一个序列中的空字符串删掉，可以这么写：

def not_empty(s):
    return s and s.strip()
#filter(not_empty, ['A', '', 'B', None, 'C', '  '])
    
#请尝试用filter()删除1~100的素数
def not_prime(x):
    if x==1:
        return True
    for tmp in range(2, x):
        if x % tmp == 0:
            return True
    return False
#filter(not_prime, range(1,101))    
    
    
# ***2-sort algorithm***
#by default, sort is in ascending order
#sorted([36, 5, 12, 9, 21])
def reversed_cmp(x, y):
    if x > y:
        return -1
    if x < y:
        return 1
    return 0
#sorted([36, 5, 12, 9, 21], reversed_cmp)

#sorted(['bob', 'about', 'Zoo', 'Credit'])
def cmp_ignore_case(s1, s2):
    u1 = s1.upper()
    u2 = s2.upper()
    if u1 < u2:
        return -1
    if u1 > u2:
        return 1
    return 0