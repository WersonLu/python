#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 二分法.py
'''


def binary_search(list, item):
    low = 0
    height = len(list) - 1

    while low <= height:
        mid = height + low
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            height = mid - 1
        else:
            low = mid + 1
    return None


my_list = list(range(1, 100))
print(binary_search(my_list, 26))

# print(list(range(1, 100)))
