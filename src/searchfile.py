# -*- coding: utf-8 -*-
"""
Created on Tue Jul 05 23:37:31 2016

@author: yumkong
"""
import os

def search(sdir, s):
    for x in os.listdir(sdir):
        
        if os.path.isfile(os.path.join(sdir, x)):
            if s in os.path.splitext(x)[0]:
                print x
        elif os.path.isdir(os.path.join(sdir, x)):
            search(os.path.join(sdir, x), s)
#def search(src, key):
#    if os.path.isfile(src):
#        if key in os.path.split(src)[1]:
#            print src
#    elif os.path.isdir(src):
#        for item in os.listdir(src):
#            itemsrc=os.path.join(src,item)
#            search(itemsrc, key)
    
    
if __name__ == '__main__':
    search(os.path.abspath('.'), 'prac')