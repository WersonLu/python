#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/6 6:35
 
'''
from PIL import ImageOps
from PIL import Image
import subprocess


def cleanFile(imagePath):
    image = Image.open(imagePath)

    image = image.point(lambda x: 0 if x < 143 else 255)

    borderImage = ImageOps.expand(image, border=20, fill='white')
    borderImage.save(imagePath)

# 收集验证码图片 保存交给这个函数处理
