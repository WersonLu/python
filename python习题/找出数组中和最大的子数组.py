#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/2/1 11:17
 
'''


def maxSubArray(self, A):
    if not A:
        return 0
    curSum = maxSum = A[0]
    for num in A[1:]:
        curSum = max(num, curSum + num)
        maxSum = max(maxSum, curSum)
    return maxSum


if __name__ == '__main__':
    list1 = [1, 3, 5, 7, -6, -4, 9]
    maxSubArray(list)
