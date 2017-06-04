# -*- coding: utf-8 -*-
"""
Created on Mon Jun 27 16:02:02 2016

@author: yumkong
"""

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

#f = lazy_sum(1,2,3,4)
#f --> function handle
#f() --> actual calculation

#可以把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y