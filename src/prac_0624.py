# -*- coding: utf-8 -*-
"""
Created on Fri Jun 24 22:42:43 2016

@author: yumkong
"""

#斐波拉契数列用列表生成式写不出来，但是，用函数把它打印出来却很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a+b
        n = n+1

#change the above ordinary function to a generator
def fib_generator(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n+1