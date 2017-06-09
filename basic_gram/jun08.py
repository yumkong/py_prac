#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 10:01:18 2017

@author: yuguang
"""
'''
(1)
swap1
there is no pointer in python, so swap through reassigning a value
'''
#def swap(a, b):
#    return (b, a)
#
#def main():
#    a = 5
#    b = 6
#    print 'before swap: a =', a, ', b =', b
#    a, b = swap(a, b)
#    print 'after swap: a =', a, ', b =', b
    
'''
(2)
swap2
alternative, send a list to swap, format param is like a reference to the list
'''
#def swap(lst):
#    # list.reverse() also applies two elements, here is for pure demonstrating
#    if len(lst) == 2:
#        tmp = lst[0]
#        lst[0] = lst[1]
#        lst[1] = tmp
#    else:
#        lst.reverse()
#               
#
#def main():
#    lst = [5, 6]
#    print 'before swap: a =', lst[0], ', b =', lst[1]
#    swap(lst)
#    print 'after swap: a =', lst[0], ', b =', lst[1]

'''
(3)
call function from another file
'''
#from jun07 import reverse_str
#
#def is_palindrome(s):
#    ''' (str) -> bool
#    Return True iff s is a palindrome
#    >>> is_palindrome('noon')
#    True
#    >>> is_palindrome('racecar')
#    True
#    >>> is_palindrome('yuguang')
#    False
#    '''
#    n = len(s)
#    # NOTE: here cannot use reverse_str(s[n/2 + 1:])
#    return s[:n/2] == reverse_str(s[n - n/2:])
#
#def main():
#    import doctest
#    doctest.testmod()
    
'''
(4)
call function from another file ==> an alternative way
'''
#import jun07
#
#def is_palindrome(s):
#    ''' (str) -> bool
#    Return True iff s is a palindrome
#    >>> is_palindrome('noon')
#    True
#    >>> is_palindrome('racecar')
#    True
#    >>> is_palindrome('yuguang')
#    False
#    '''
#    n = len(s)
#    # NOTE: here cannot use reverse_str(s[n/2 + 1:])
#    return s[:n/2] == jun07.reverse_str(s[n - n/2:])
#
#def main():
#    import doctest
#    doctest.testmod()    
  
'''
(5)
compare doctest and unittest: this is doctest
NOTE: the doctest is sensitive to spaces!!! It compares literally to the strings in doc
e.g. [1, 2, 3] != [1,2,3] ==> due to lack of spaces in later, but they are actually the same
'''  
#def remove_shared(L1, L2):
#    '''
#    Remove items from L1 that are in both L1 and L2.
#    >>> list1 = [1, 2, 3, 4, 5, 6]
#    >>> list2 = [2, 4, 5, 7]
#    >>> remove_shared(list1, list2)
#    >>> list1
#    [1, 3, 6]
#    >>> list2
#    [2, 4, 5, 7]
#    '''
#    for ch in L2:
#        if ch in L1:
#            L1.remove(ch)
#            
#def main():
#    import doctest
#    doctest.testmod()    

'''
(6)
compare doctest and unittest: this is unittest
NOTE: the unittest is insensitive to spaces ==> more flexible
''' 
#import unittest   #doctest
# 
#def remove_shared(L1, L2):
#    '''
#    Remove items from L1 that are in both L1 and L2.
#    >>> list1 = [1, 2, 3, 4, 5, 6]
#    >>> list2 = [2, 4, 5, 7]
#    >>> remove_shared(list1, list2)
#    >>> list1
#    [1, 3, 6]
#    >>> list2
#    [2, 4, 5, 7]
#    '''
#    for ch in L2:
#        if ch in L1:
#            L1.remove(ch)
#
#class TestRemoveShared(unittest.TestCase):
#    ''' Tests for remove_shared. '''
#    # NOTE: test method must begin with 'test', not recomment to begin with others: 'Test' or ...
#    def test_general_case(self):
#        list1 = [1, 2, 3, 4, 5, 6]
#        list2 = [2, 4, 5, 7]
#        list1_expect = [1,3,6]
#        list2_expect = [2,4, 5, 7]
#        remove_shared(list1, list2)
#        # test body
#        self.assertEqual(list1, list1_expect)
#        self.assertEqual(list2, list2_expect)
#          
#def main():
#    #import unittest   #doctest
#    ''' The following will call the method defined in unittest child class '''
#    unittest.main(exit = False)               
         
'''
(7)
linear search
'''    
#def linear_search(L, v):
#    ''' (list, obj) -> int
#    Return the index of the 1st occurence of v in L
#    or -1 if v is not in L
#    >>> linear_search([2,3,4,3], 2)
#    0
#    >>> linear_search([2,3,4,3], 3)
#    1
#    >>> linear_search([2, 3, 5, 3], 8)
#    -1
#    '''
#    i = 0
#    n = len(L)
#    while i < n and L[i] != v:
#        i += 1
#    if i == len(L):
#        return -1
#    else:
#        return i

'''
(8)
binary search
'''  
#def binary_search(L, v):
#    ''' (list, object) -> int
#    Precondition: L is sorted from smallest to largest
#    Return the index of the 1st occurence of v in L
#    or -1 if v is not in L
#    >>> binary_search([2,3,3,4], 2)
#    0
#    >>> binary_search([2,3,3,4], 3)
#    1
#    >>> binary_search([2, 3, 3, 4], 8)
#    -1
#    >>> binary_search([2, 3, 3, 4], 0)
#    -1
#    '''
#    top = len(L) - 1
#    bot = 0
#    
#    while bot <= top:
#        mid = (bot + top) / 2
#        if L[mid] < v:
#            bot = mid + 1
#        else:
#            top = mid - 1
#
#    if bot == len(L) or L[bot] != v:
#        return -1
#    else:
#        return bot
        

'''
(9)
binary search2
'''

def binary_search2(L, v):
    ''' (list, object) -> int
    Precondition: L is sorted from smallest to largest
    Return the index of the ***LAST*** occurence of v in L
    or -1 if v is not in L
    >>> binary_search2([1,2,3,3,4], 2)
    1
    >>> binary_search2([1,2,3,3,4], 3)
    3
    >>> binary_search2([1,2,3,3,4], 8)
    -1
    >>> binary_search2([1,2,3,3,4], 0)
    -1
    '''
    top = len(L) - 1
    bot = 0
    while bot <= top:
        mid = (bot + top) / 2
        if L[mid] <= v:
            bot = mid + 1
        else:
            top = mid - 1
    if L[top] != v or top == -1:
        return -1
    else:
        return top
    
def main():
    import doctest
    doctest.testmod()
    
if __name__ == '__main__':
    main()