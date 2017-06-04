# -*- coding: utf-8 -*-
"""
Created on Fri Jul 01 17:05:59 2016

@author: yumkong
"""

import unittest

from mydict import Dict

class TestDict(unittest.TestCase):
    
    def setUp(self):
        print 'setUp...'
        
    def tearDown(self):
        print 'tearDown...'
    
    def test_init(self):
        d = Dict(a=1, b = 'test')
        self.assertEquals(d.a, 1)
        self.assertEquals(d.b, 'test')
        self.assertTrue(isinstance(d, dict))
        
    def test_key(self):
        d = Dict()
        d['key'] = 'value'
        self.assertEquals(d.key, 'value')
    
    def test_attr(self):
        d = Dict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEquals(d['key'], 'value')
        
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']
            
    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
            
#run the unit test
if __name__ == '__main__':
    unittest.main()