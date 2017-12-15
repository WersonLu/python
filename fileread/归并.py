#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/8 15:11
 
'''
mylist1=[11,2,-4,7,-23,5]
mylist2=[2,4,6,8,3]
mylist1.sort()
mylist2.sort()
print(mylist1)
print(mylist1[::2])
print(sorted(mylist1,key=abs))
