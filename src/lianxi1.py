# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 17:15:49 2014

@author: yumkong
"""
#(1)
#total = 0
#count = 0
#
#while True:
#    inp = input('Enter a number:')
#    if inp == 'done': break
#    value = float(inp)
#    total = total + value
#    count = count + 1
#
#average = total/ count
#print('Average:', average)

##(2)
#fname = input("Enter file name: ")
#fh = open(fname)
#lst = list()
#for line in fh:
#    a = line.split()
#    for words in a:
#        if words not in lst:
#            lst.append(words)
#     
#lst.sort()
#print(lst)

#(3)
#fname = input("Enter file name: ")
#if len(fname) < 1 : fname = "mbox-short.txt"
#
#fh = open(fname)
#count = 0
#
#for line in fh:
#    #make sure not to include lines starting with 'From:'
#    if line.startswith('From '):
#        a = line.split()
#        print(a[1])
#        count = count + 1
#
#print("There were", count, "lines in the file with From as the first word")
#

#4
#counts = dict()
#names = ['csev','cwen','csev','zqian','cwen']
#for name in names:
#    if name not in counts:
#        counts[name] = 1
#    else:
#        counts[name] = counts[name] + 1
#print(counts)
##either create with default value as key value or update
#print(counts.get('csev',0)) #default value is 0
#
#counts2 = dict()
#for name in names:
#    counts2[name] = counts2.get(name,0) + 1
#print(counts2)

#counts3 = dict()
#print('Enter a line of text:')
#line = input('');
#words = line.split()
#print('Words:', words)
#print('Counting...')
#for word in words:
#    counts3[word] = counts3.get(word,0) + 1
#print('Counts:',counts3);
#for key in counts3:
#    print(key, counts3[key])
#print(list(counts3))
#print(counts3.keys())
#print(counts3.values())
#print(counts3.items())
##2 iteration values
#for a,b in counts3.items():
#    print(a,b)
#bigcount = None
#bigword = None
#for word,count in counts3.items():
#    if bigcount is None or count > bigcount:
#        bigword = word
#        bigcount = count
#print(bigword, bigcount)

# 5
name = input("Enter file:")
if len(name) < 1 : name = "../data/mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    #make sure not to include lines starting with 'From:'
    if line.startswith('From '):
        a = line.split()
        counts[a[1]] = counts.get(a[1],0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print(bigword, bigcount)

#Write a program to read through the mbox-short.txt and figure out the distribution by hour
#name = input("Enter file:")
#if len(name) < 1 : name = "../data/mbox-short.txt"
#handle = open(name)
#counts = dict()
## use the follows to get each line of the file
#for line in handle:
#    #make sure not to include lines starting with 'From:'
#    if line.startswith('From '):
#        #the whole line        
#        a = line.split()
#        #time: hour minute seconds
#        hour = a[5].split(':')
#        #hour
#        counts[hour[0]] = counts.get(hour[0],0) + 1
## put dict to list to ease the following sorting process
#lst = list()
#for hour,count in counts.items():
#    lst.append((hour, count))
## sort the list, if list is a tuple, sort it by the first element in tuple
#lst.sort()
#for hour, count in lst:
#    print(hour, count)