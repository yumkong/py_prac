# -*- coding: utf-8 -*-
"""
Created on Sun Jul 03 21:23:57 2016

@author: yumkong
"""

try:
    print 'try...'
    r = 10 / 10
    print 'result:', r
except ZeroDivisionError, e:
    print 'except:', e
finally:
    print 'finally...'
print 'END'

#如果没有错误发生，可以在except语句块后面加一个else，
#当没有错误发生时，会自动执行else语句：
try:
    print 'try...'
    r = 10 / int('a')
    print 'result:', r
except ValueError, e:
    print 'ValueError:', e
except ZeroDivisionError, e:
    print 'ZeroDivisionError:', e
else:
    print 'no error!'
finally:
    print 'finally...'
print 'END'

def foo(s):
    return 10 / int(s)
def bar(s):
    return foo(s) * 2
def main1():
    try:
        bar('0')
    except StandardError, e:
        print 'Error!', e
#    except ZeroDivisionError, e:
#        print 'ZeroDivisionError:', e
    finally:
        print 'finally...'
main1()

#if __name__ == '__main__':
#    main()

#Python内置的logging模块可以非常容易地记录错误信息：
#同样是出错，但程序打印完错误信息后会继续执行，并正常退出
# the effect of following code can only be seen in command line:
#python error_and_debug.py
import logging

def foo1(s):
    return 10 / int(s)

def bar1(s):
    return foo1(s) * 2

def main():
    try:
        bar1('0')
    except StandardError, e:
        logging.exception(e)

main()
print 'END'
