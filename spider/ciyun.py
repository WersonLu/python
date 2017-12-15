#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu
 
@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.
 
@contact: wersonliugmail.com
 
@software: garner
 
@file: ciyun.py
 
@time: 2017/12/4 17:57
 
@desc:
 
'''
from os import path
from scipy.misc import imread
import matplotlib.pyplot as plt
import jieba
from wordcloud import WordCloud

f = open('f:/iphone.txt', 'r')
text = f.read()

cut_text = ''.join(jieba.lcut(text))
print(cut_text)
color_msk = imread("iphone.jpg")
cloud = WordCloud(
    background_color='white',
    mask=color_msk,
    max_words=200,
    max_font_size=5000
)
word_cloud = cloud.generate(cut_text)
plt.imshow(word_cloud)
plt.axis('off')
plt.show()
