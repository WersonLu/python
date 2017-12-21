#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/20 10:55
 
'''
user_input = input("你的输入是")
for filter_word in open('test1.txt', encoding='UTF-8'):

    fw = filter_word.strip()  # 把文本以空格分开
    if fw in user_input:  # 敏感词在输入内容中
        fw_len = len(fw)  # 计算长度
        user_input = user_input.replace(fw, '*' * fw_len)  # 把敏感词替换成*
    else:
        pass
print(user_input)
