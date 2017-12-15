#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/6 12:42
 
'''

import re

pattern = re.compile(r'\d+')
result = re.match(pattern, '129abc')  # match 只会从string开头位置匹配没有返回none
result2 = re.search(pattern, 'abc586de')  # search 会扫描整个string
result3 = re.split(pattern, 'a1d3f4')  # split 按照匹配的子串切割后返回列表
result4 = re.findall(pattern, 'a1d3f4')  # findall 返回匹配的子串
result5 = re.finditer(pattern, 'a1d3f4')  # finditer  以迭代器的形式返回子串

print(result.group())  # .group()可以获取捕获的值 groups()返回元组 gruopdict()返回字典
print(result2.group())
print(result3)  # --> ['a', 'd', 'f', '']
print(result4)  # -->['1', '3', '4']
for match in result5:
    print(match.group())
