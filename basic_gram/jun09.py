#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  9 15:14:23 2017

@author: yuguang
"""
'''
Define a class and its methods
'''

class CashRegister:
    ''' A cash register. '''
    def __init__(self, ones, twos, fives, tens, twenties):
        ''' (CashRegister, int, int, int, int, int) -> NoneType
        A CashRegister with ones, twos, fives, tens and twenties
        >>> register = CashRegister(5, 5, 5, 5, 5)
        >>> register.ones
        5
        >>> register.twos
        5
        >>> register.fives
        5
        >>> register.tens
        5
        >>> register.twenties
        5
        '''
        self.ones = ones
        self.twos = twos
        self.fives = fives
        self.tens = tens
        self.twenties = twenties
    
    def __str__(self):
        ''' (CashRegister) -> str
        Return a string representation of this CashRegister.
        >>> reg1 = CashRegister(1,2,3,4,5)
        >>> reg1.__str__()
        'CashRegister: $160 ($1x1, $2x2, $5x3, $10x4, $20x5)'
        '''
        return 'CashRegister: ' + \
               '${0} ($1x{1}, $2x{2}, $5x{3}, $10x{4}, $20x{5})'.format(
                       self.get_total(), self.ones, self.twos,
                       self.fives, self.tens, self.twenties)
              
    def __eq__(self, other):
        ''' (CashRegister, CashRegister) -> bool
        Return True iff this CashRegister has the same amount of money as other.
        >>> reg1 = CashRegister(10, 0, 5, 5, 5)
        >>> reg2 = CashRegister(0, 5, 5, 5, 5)
        >>> reg1 == reg2
        True
        '''
        return self.get_total() == other.get_total()
    
    def get_total(self):
        ''' (CashRegister) -> int
        Return the total amount of cash in the register.
        >>> register = CashRegister(5,5,5,5,5)
        >>> register.get_total()
        190
        '''
        return self.ones + self.twos * 2 + self.fives * 5 + \
               self.tens * 10 + self.twenties * 20
    
    def add(self, count, name):
        ''' (CashRegister, int, str) -> NoneType
        Add count items of name to the register.
        name is one of 'ones','twos','fives','tens', and 'twenties'.
        >>> reg1 = CashRegister(1,2,3,4,5)
        >>> reg1.add(2, 'twos')
        >>> reg1.twos
        4
        '''
        # NOTE python has no switch/case clause
        if name == 'ones':
            self.ones += count
        elif name == 'twos':
            self.twos += count
        elif name == 'fives':
            self.fives += count
        elif name == 'tens':
            self.tens += count
        elif name == 'twenties':
            self.twenties += count
        else:
            print 'Wrong item name!'
        
    def remove(self, count, name):
        ''' (CashRegister, int, str) -> NoneType
        Remove count items of name to the register.
        name is one of 'ones','twos','fives','tens', and 'twenties'.
        >>> reg1 = CashRegister(1,2,3,4,5)
        >>> reg1.remove(2, 'twos')
        >>> reg1.twos
        0
        '''
        if name == 'ones':
            self.ones -= count
        elif name == 'twos':
            self.twos -= count
        elif name == 'fives':
            self.fives -= count
        elif name == 'tens':
            self.tens -= count
        elif name == 'twenties':
            self.twenties -= count
        else:
            print 'Wrong item name!'

if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
    reg = CashRegister(5,5,5,5,5)
    print(reg.get_total())
    
    reg.add(2, 'ones')
    reg.remove(3, 'twos')
    print(reg.get_total())
    
    reg1 = CashRegister(2,0,0,0,0)
    reg2 = CashRegister(0,1,0,0,0)
    reg3 = CashRegister(1,1,0,0,0)
    print(reg1)
    print(reg2)
    print(reg1 == reg2)
    print(reg2 == reg3)
            