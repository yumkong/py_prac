#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 29 21:10:24 2016

@author: yumkong
"""

'a test module'

__author__ = 'Yuguang Liu'

import sys

def test():
    args = sys.argv
    # 1: no arguments except args[0] = .py itself
    if len(args) == 1:
        print 'Hello world'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

# 作用域
#private function, should not be cited outside
def _private_1(name):
    return 'Hello, %s' % name
#private function, should not be cited outside
def _private_2(name):
    return 'Hi, %s' % name
#public function, can be called outside
def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

import Image
im = Image.open('v1.jpg')
print im.format, im.size, im.mode
im.thumbnail((200,100))
im.save('thumb.jpg', 'JPEG')

if __name__ == '__main__':
    test()
