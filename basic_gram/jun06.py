#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 09:48:07 2017

@author: yuguang
"""

'''
(1)
calling a local function with lst as params
'''
#def appendsum(lst):
#    #repeatedly append the sum of current last 3 elems of a list
#    # list can be changed in the local func, but ordinary type cannot
#    for i in range(25):
#        lst.append(lst[-1] + lst[-2] + lst[-3])
#        
#def main():
#    sum_thr = [0, 1, 2]
#    appendsum(sum_thr)
#    print sum_thr

'''
(2)
a simple class
'''
#class BankAccount:
#    #define a bank account class
#    def __init__(self, initial_balance):
#        #like a constructor in C++, initialize all member variables
#        self.balance = initial_balance
#        self.fee = 0
#    def deposit(self, amount):
#        # self is like this* in C++
#        self.balance += amount
#    def withdraw(self, amount):
#        ''' 
#        withdraw the amount from the account
#        if resulting a negative balance, deducts a penalty fee of $5
#        '''
#        self.balance -= amount
#        if self.balance < 0:
#            self.fee += 5
#            self.balance -= 5
#    def get_balance(self):
#        return self.balance
#    def get_fees(self):
#        return self.fee
#    
#def main():
#    myacc = BankAccount(10)
#    myacc.withdraw(15)
#    myacc.deposit(20)
#    print 'balance = ', myacc.get_balance()
#    print 'fees = ', myacc.get_fees()
  
'''
(3)
about return value of a func
'''   
#def fahren2cel(fval):
#    cval = (5.0/9) * (fval-32)
#    return cval
#
#def fahren2cel_noret(fval):
#    # format param copy the real param, but does not change the real param
#    fval = (5.0/9) * (fval-32)
#    
#def hello():
#    print "hello, world!"
#
#def main():
#    print fahren2cel(200)
#    # if a function has no explicit return, return None
#    print fahren2cel_noret(200)
#    fval2 = 200
#    fahren2cel_noret(fval2)
#    print 'new fval =', fval2
#    
#    hello()
#    print hello() #first call hello(), then print the return val
  
'''
(4)
flexibility of python funcs
'''
#def add_num(a, b):
#    return a+b
#
#def main():
#    print add_num(4,5)
#    print add_num(4.2, 6.6)
#    print add_num(4, 6.6)
#    print add_num(4.2, 6)
#    print add_num([4], [4,5])  #ok, '+' is reloaded as a concat operator of 2 lists
#    #print add_num(4, [4,5])  #err, '+' not support 1 list and 1 int
#    #print add_num(4.2, 's') #err, '+' not support 1 float and 1 str as oprands
#    print add_num('yum', 'kong') #ok: '+' is reloaded as a concat operator of 2 strs

'''
(5)
local and global scope for variables
'''
#a = 3
#b = 6
#
#'''
#in the case of the following function
#a,b,foo occur in the global scope
#a,c occur in the local scope (NOTE: this a is not the global a)
#'''
#def foo(a):
#    '''
#    if b is locally defined, use the local b
#    otherwise, here, since b is not defined inside the func, it will search global var b 
#    '''
#    c = a + b 
#    return c
#
#def main():
#    '''
#    err: a is a param, so a local variable, 
#    cannot recognize global var with the same name
#    '''
#    # print foo()  #err 
#    print foo(66)
#    print foo(a)
#    print foo(b)
#    print foo(a+b)
    
'''
(6)
which type can be the key of a dict?
==> keys in a python dict must be immutable
'''
#def main():
#    #define an empty dictionary
#    mydict = dict()
#    
#    ''' all oks '''
#    mydict[66] = 1  #int can be the key
#    mydict[1.6] = 23 #float can be the key
#    mydict[None] = 456 #NoneType can be the key
#    mydict[False] = 2 #bool type can be the key
#    mydict[""] = 3 # str type can certainly be the key
#    mydict[(1,2)] = 3 # tuple can certainly be the key
#    print mydict
#    ''' all errs '''
#    #mydict[[]] = 4 #err: list cannot be key 
#    #mydict[{}] = 43 #err: dict cannot be key 
#    #mydict[set([])] = 433 #err: dict cannot be key 

'''
(7)
two simple functions
'''
# need to use pi and tan() from this library
import numpy as np

def foo(x):
    return -5 * (x ** 5) + 69 * x * x - 47

def calc_regular_polygon_area(n, s):
    # n: #sides, s:side length
    return 0.25 * n * s * s / np.tan(np.pi / n)

def main():
    print foo(0), foo(1), foo(2), foo(3)
    print calc_regular_polygon_area(7, 3)
    

if __name__ == '__main__':
    main()
