#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 11:29:31 2017

@author: yuguang
"""

'''
(1) bubble sort
'''

#def bubble_sort(L):
#    ''' (List) -> NoneType
#    sort the items of L from smallest to largest.
#    >>> L = [6, 4, 5, 7, 89, 0, 32]
#    >>> bubble_sort(L)
#    >>> L
#    [0, 4, 5, 6, 7, 32, 89]
#    '''
#    len_minus_one = len(L) - 1
#    # there are more than 2 elements
#    while len_minus_one != 0:
#        # each time move the largest element to the end
#        for i in range(len_minus_one):
#            if L[i] > L[i+1]:
#                L[i], L[i+1] = L[i+1], L[i]
#                
#        len_minus_one -= 1

'''
(2) insert sort
'''
#def insert(L, i):
#    ''' (list, int) -> NoneType
#    Precondition: L[:i] is sorted from smallest to largest.
#    Move L[i] to where it belongs in L[:i+1].
#    >>> L = [7, 3, 5, 2]
#    >>> insert(L, 1)
#    >>> L
#    [3, 7, 5, 2]
#    '''
#    value = L[i]
#    j = i
#    while j != 0 and L[j - 1] > value:
#        L[j] = L[j - 1]
#        j = j - 1
#    L[j] = value
#
#def insertion_sort(L):
#    ''' (list) -> NoneType
#    Sort the items of L from smallest to largest.
#    >>> L = [7, 3, 5, 2]
#    >>> insertion_sort(L)
#    >>> L
#    [2, 3, 5, 7]
#    '''
#    n = len(L)
#    for i in range(n):
#        insert(L, i)    

'''
(3) selection sort
'''
#def get_index_of_smallest(L, i):
#    ''' (List, int) -> int
#    Return the index of the smallest item in L[i:].
#    >>> get_index_of_smallest([2, 7, 3, 5], 1)
#    2
#    '''
#    index_of_smallest = i
#    for j in range(i+1, len(L)):
#        if L[j] < L[index_of_smallest]:
#            index_of_smallest = j
#    return index_of_smallest
#
#def selection_sort(L):
#    ''' (list) -> NoneType
#    Sort the items of L from smallest to largest.
#    >>> L = [7, 3, 5, 2]
#    >>> insertion_sort(L)
#    >>> L
#    [2, 3, 5, 7]
#    '''
#    for i in range(len(L)):
#        index_of_smallest = get_index_of_smallest(L, i)
#        L[index_of_smallest], L[i] = L[i], L[index_of_smallest]  
        
'''
(4) Quick sort
'''
def quick_sort(L):
    ''' (list) -> list
    Given L, return the sorted list from smallest to largest.
    >>> L = [9,8,7,6,5,4,3,2,1,88,66]
    >>> quick_sort(L)
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 66, 88]
    '''
    if len(L) <= 1:
        return L
    else:
        mid = L[len(L) / 2]
        left = [x for x in L if x < mid]
        middle = [x for x in L if x == mid]
        right = [x for x in L if x > mid]
        return quick_sort(left) + middle + quick_sort(right)
    
def main():
    import doctest
    doctest.testmod()

if __name__ == '__main__':
    main()