#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/20 10:44
 
'''
# 统计任意英文文本的单词

import re

file_name = 'test.txt'

lines_count = 0
words_count = 0
chars_count = 0
words_dict = {}
lines_list = []

with open(file_name, 'r')as f:
    for line in f:
        lines_count = lines_count + 1
        chars_count = chars_count + len(line)
        match = re.findall(r'[^a-zA-Z0-9]+', line)
        for i in match:
            line = line.replace(i, ' ')
        lines_list = line.split()
        for i in lines_list:
            if i not in words_dict:
                words_dict[i] = 1
            else:
                words_dict[i] = words_dict[i] + 1
print(len(words_dict))
print(lines_count)
print(chars_count)

for k, v in words_dict.items():
    print(k, v)
