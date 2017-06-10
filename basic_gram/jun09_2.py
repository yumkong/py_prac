#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 16:54:18 2017

@author: yuguang
"""

'''
Getting started with numpy, scipy and matplotlib
'''

'''
(1) numpy + matplotlib
'''
#import numpy as np
#import matplotlib.pyplot as plt
#
#x = np.array([1, 2, 3, 6])
## like python's range, but returns an array 
#y = np.arange(4)
## create an array with 4 eually spaced points starting with 0 and ending with 6
#z = np.linspace(0, 6, 4)
#
#a = np.linspace(-np.pi, np.pi, 100)
#b = np.sin(a)
#c = np.cos(a)
#
#p1, = plt.plot(a, b, label="Line 1", linestyle = '--')
#p2, = plt.plot(a, c, label="Line 2", linewidth = 4)
#plt.legend([p1, p2], ['sin', 'cos'])
#plt.show()

'''
(2) 3 methods for formatted output
'''
#fmt1 = '%s %s %d' % ('hello', 'world', 666)
#print fmt1
#fmt2 = '{0} {1} {2}'.format('hello', 'world', 666)
#print fmt2
#fmt3 = 'hello world ' + str(666)
#print fmt3

'''
(3) some funcs for str
'''
s = 'hello'
print s.capitalize()
print s.upper()
print s.rjust(7, '*')
print s.ljust(7, '@')
print s.replace('l', '(abc)')
print ' world  '.strip() #strip leading and trail spaces