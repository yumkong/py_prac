#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 10:31:51 2017

@author: yuguang
"""

'''
(1)
palindrome 1 --> how to write doctest
'''
#def is_palindrome_v1(s):
#    ''' (str) -> bool
#    Return True iff s is a palindrome
#    >>> is_palindrome_v1('noon')
#    True
#    >>> is_palindrome_v1('racecar')
#    True
#    >>> is_palindrome_v1('yumkong')
#    False
#    '''
#    return reverse_str(s) == s
#
#def reverse_str(s):
#    ''' (str) -> str
#    Return a reversed version of s.
#    >>> reverse_str('hello')
#    'olleh'
#    >>> reverse_str('a')
#    'a'
#    '''
#    rev = ''
#    # add each character to the beginning of rev
#    for ch in s:
#        rev = ch + rev
#    return rev

'''
(2)
palindrome 2
'''
#def is_palindrome_v2(s):
#    ''' (str) -> bool
#    Return True iff s is a palindrome
#    >>> is_palindrome_v2('noon')
#    True
#    >>> is_palindrome_v2('racecar')
#    True
#    >>> is_palindrome_v2('yumkong')
#    False
#    '''
#    n = len(s)
#    return s[:n/2] == reverse_str(s[n - n/2:])
#
#def reverse_str(s):
#    ''' (str) -> str
#    Return a reversed version of s.
#    >>> reverse_str('hello')
#    'olleh'
#    >>> reverse_str('a')
#    'a'
#    '''
#    rev = ''
#    # add each character to the beginning of rev
#    for ch in s:
#        rev = ch + rev
#    return rev

'''
(3)
palindrome 3
'''
#def is_palindrome_v3(s):
#    ''' (str) -> bool
#    Return True iff s is a palindrome
#    >>> is_palindrome_v3('noon')
#    True
#    >>> is_palindrome_v3('racecar')
#    True
#    >>> is_palindrome_v3('yumkong')
#    False
#    '''
#    n = len(s)
#    for i in range(n/2 + 1):
#        if s[i] != s[n-1-i]:
#            return False
#    return True

'''
(4)
check whether a dict is a one-to-one mapping
'''
def is_one_to_one(d):
    ''' (dict) -> pool
    Return True iff no two of d's keys map to the same value.
    
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 3})
    True
    >>> is_one_to_one({'a': 1, 'b': 2, 'c': 1})
    False
    '''
    d_vals = d.values()
    # set automatically remove duplicated elements
    d_vals_set = set(d_vals)
    return len(d_vals) == len(d_vals_set)

if __name__ == '__main__':
    import doctest
    doctest.testmod()