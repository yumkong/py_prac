# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 16:27:53 2016

@author: yumkong
"""

#def now():
#    print '2016-06-29'
# assign the function to a variable, making the variable a function object:
#f = now
# call the fuction
#f()
    
#函数对象有一个__name__属性，可以拿到函数的名字：
#now.__name__
#f.__name__
    
#在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
#本质上，decorator就是一个返回函数的高阶函数。
#所以，要定义一个能打印日志的decorator，可以定义如下：
def log(func):
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
    
#by default, the function name right after @log, namely now would be passed
# to log as arguments
# putting @log at the beginning of now()'s definition is equivalent to
# executing now = log(now)
@log
def now():
    print '2013-12-25'
    
#一个完整的decorator的写法如下：
import functools

def log_complete(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'call %s():' % func.__name__
        return func(*args, **kw)
    return wrapper
@log_complete
def now1():
    print '2016-12-25'

#针对带参数的decorator：
def log_complete_arg(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % (text, func.__name__)
            return func(*args, **kw)
        return wrapper
    return decorator
@log_complete_arg('liu')
def now2():
    print '2016-12-25'
    
#question 1:
#请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志
def log_prac1(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print 'begin call %s():' % func.__name__
        r = func(*args, **kw)
        print 'end call %s():' % func.__name__
        return r
    return wrapper
@log_prac1
def now3():
    print '2016-06-25'

#question2:
#能否写出一个@log的decorator，使它既支持：
#@log
#def f():
#    pass
#又支持：
#@log('execute')
#def f():
#    pass
def log_prac2(text):
    if callable(text):
        #callable means text is a function name
        func = text
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print '%s %s():' % ('no text',func.__name__)
            return func(*args, **kw)
        return wrapper
    else:
        # text is not a function name, so add a decorator function
        def decorator(func):
            @functools.wraps(func)
            def wrapper(*args, **kw):
                print '%s %s():' % (text, func.__name__)
                return func(*args, **kw)
            return wrapper
        return decorator
@log_prac2('execute')
def f():
    pass
@log_prac2
def f1():
    pass
#so can call both(1): f() and (2): f1()

# ----partial function-----
def int2(x, base = 2):
    return int(x, base)

int2_partialfunc = functools.partial(int, base = 2)
#int2_partialfunc('111')
#int2_partialfunc('111', base = 10)