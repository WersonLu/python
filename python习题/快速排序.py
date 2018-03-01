#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/2/28 23:43
 
'''


def partiton(li, a, b):
    x = li[b]
    i = a
    for j in range(a, b):
        if li[j] < x:
            li[i], li[j] = li[j], li[i]
            i += 1
    li[i], li[b] = li[b], li[i]
    return i


def quict_sort(li, a, b):
    if a >= b:
        return
    i = partiton(li, a, b)
    quict_sort(li, a, i - 1)
    quict_sort(li, i + 1, b)


li = [23, 45, 34, 67, 23, 89, 33, 22]
quict_sort(li, 0, len(li) - 1)
print(li)


# 方法二
def quick_sort(lists, left, right):
    if left > right:
        return lists
    low, high = left, right
    key = lists[left]  # key即是标准数
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort(lists, low, left - 1)
    quick_sort(lists, right + 1, high)
    return lists
