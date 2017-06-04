# -*- coding: utf-8 -*-
"""
Created on Mon Jul 04 22:14:43 2016

@author: yumkong
"""

# method 1
#f = open('romeo.txt', 'r')
#f.read()
#f.close()

# in case IO error, f.close() will not be called, so change like this:
#try:
#    f = open('romeo.txt', 'r')
#    # f.read() returns a string
#    print f.read()
#finally:
#    # if f is valid (not zero)
#    if f:
#        f.close()

# method 3, try finally is too complex, make it simpler:
#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法。
with open('romeo.txt', 'r') as f:
    #(1)    
    #print f.read()
    # (2)    
    #print f.readline()
    #print f.readline()
    #print f.readline()
    #print f.readline()
    #(3)
    #print f.readlines()
    
    #(4)
    for line in f.readlines():
        print(line.strip()) # 把末尾的'\n'删掉,因为print会自动换行的
        
# read binary file
#f = open('thumb.jpg','rb')
#f.read()
        
# write file, 如果打开的文件已有内容，会把其覆盖
with open('romeo.txt', 'w') as f:
    f.write('Hello, world!')