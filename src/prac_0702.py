# -*- coding: utf-8 -*-
"""
Created on Sat Jul 02 11:53:04 2016

@author: yumkong
"""

#定制类
#(1)  __str__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name: %s)' % self.name
    __repr__ = __str__
    
#(2) __iter__
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 #initializa two counters, a and b
    def __iter__(self):
        return self #实例本身就是迭代对象，故返回自己
    def next(self):
        self.a, self.b = self.b, self.a + self.b #calculate the next value
        if self.a > 100000:
            raise StopIteration()
        return self.a
# for n in Fib():
#    print n
        
#(3) __getitem__
class Fib2(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
# implement the slice effect as in list:
#__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib3(object):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a+b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a+b
            return L
#f = Fib()
#f[0:5]
#注意以上并不完整：没有对step参数作处理：也没有对负数作处理
#所以要正确实现一个__getitem__()还是有很多工作要做的。
            
#(4)：__getattr__
class Student2(object):
    def __init__(self):
        self.name = 'Liu'
    def __getattr__(self, attr):
        #use obj.score to get
        if attr == 'score':
            return 99
        #use obj.age() to get, because it is a default function
        if attr == 'age':
            return lambda: 25
        #for other attrs, return standard error hint
        raise AttributeError('\'Student2\' object has no attribute \'%s\''%attr)

#(5): __call__
class Student3(object):
    def __init__(self):
        self.name = 'Liu'
    def __call__(self, age=6):
        print('My name is %s, and I\'m %d years old.'% (self.name, age) )
#s = Student('Michael')
#s()