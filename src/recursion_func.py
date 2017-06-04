# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 17:39:20 2016

@author: yumkong
"""

#递归函数的优点是定义简单，逻辑清晰。
#理论上，所有的递归函数都可以写成循环的方式，但循环的逻辑不如递归清晰。
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)