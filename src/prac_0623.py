# -*- coding: utf-8 -*-
"""
Created on Thu Jun 23 16:40:33 2016

@author: yumkong
"""
# arguments are variable, 0 or many
#calc(*[1,3,3]) ==> variable argument, by adding a star mark before a list
#calc(1,3,3)
#calc()
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

# arguments are invariable: must contain exactly 1 argument (tuple or list)
def calc_invariable(numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
    
#可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
#而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name, age, **kw):
    print 'name:', name, 'age:', age, 'other:', kw
    
#参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。
#eg: args = (1, 2, 3, 4)
#    kw = {'x': 99}
#    func(*args, **kw)
def func(a, b, c=0, *args, **kw):
    print 'a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw
    