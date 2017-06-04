# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 16:59:19 2016

@author: yumkong
"""

#编写一个Dict类，这个类的行为和dict一致，但是可以通过属性来访问，用起来就像下面这样
#d = Dict(a=1, b=2)
#d['a']
#d.a

# a self-defined Dict class, inheriting from standard dict class
class Dict(dict):
    #??? what does this function mean 
    def __init__(self, **kw):
        #super(Dict, self) -- get the super class of Dict
        super(Dict, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value