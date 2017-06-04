# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 10:07:03 2016

@author: yumkong
"""
# (object) --> 表示student类继承自object类
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def print_score(self):
        print '%s: %s' % (self.name, self.score)
        
# 变量前加双下划线，就可以变成私有变量：
class Student_private(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
        
    def print_score(self):
        print '%s: %s' % (self.__name, self.__score)
    #通过method给私有变量赋值的好处是可以判断传入值是否有效：
    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

#继承和多态
class Animal(object):
    def run(self):
        print 'Animal is running'

class Dog(Animal):
    #可以把父类不适合的方法覆盖重写
    def run(self):
        print 'Dog is running'
    #也可以新增自己特有的方法
    def eat(self):
        print 'eating meat'
    def __len__(self):
        return 100
class Cat(Animal):
    def run(self):
        print 'Cat is running'

def run_twice(animal):
    animal.run()
    animal.run()
    
#run_twice(Cat())
#run_twice(Dog())
#run_twice(Animal())
#run_twice(list()) --> false, list has no attribute run
    
#a = list()
#b = Animal()
#c = Dog()
#isinstance(a,list)
#isinstance(b, Animal)
#isinstance(c, Dog)
#isinstance(c, Animal)
    
#using __slot__ to restrict a class's attributes
class Student_slot(object):
    __slots__ = ('name', 'score')
# liu = Student_slot()
# liu.hi = 'hei'
    
# Python内置的@property装饰器就是负责把一个方法变成属性调用的
class Student_pro(object):
    #把一个getter方法变成属性，只需要加上@property就可以
    @property
    def score(self):
        return self._score
    #把一个setter方法变成属性赋值
    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
    #还可以定义只读属性:只定义getter方法，不定义setter方法就是一个只读属性
    @property
    def age(self):
        return 2000 - self._score