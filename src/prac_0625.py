# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 08:29:07 2016

@author: yumkong
"""

def f(x):
    return x*x
#map(f, range(10))
#map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9])
    
def fn(x, y):
    return x * 10 + y
    
#reduce(fn, [1,2,3,4,5])
    
def fn1(x, y):
    return x * 10 + y

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

#reduce(fn1, map(char2num, '13579'))

#整理成一个str2int的函数就是：

def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
    return reduce(fn, map(char2num, s))
    
#还可以用lambda函数进一步简化成：

def char2num1(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
def str2int1(s):
    return reduce(lambda x,y: x*10+y, map(char2num1, s))

# practice1 solution
def firstLetterUpper(L):
    def fn(L1):
        return L1[0].upper() + L1[1:].lower()
    return map(fn, L)
#firstLetterUpper(['adam', 'LISA', 'barT'])
    
# practice2 solution
def prod(L):
    def multiply(x, y):
        return x*y
    return reduce(multiply, L)