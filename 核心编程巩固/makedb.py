#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : demo4.py
'''

# from .demo5 import Person, Manager
from demo5 import Person, Manager

bob1 = Person('Bob Smith')
sue1 = Person('Sue Jones', job='dev', pay=10000)
tom1 = Manager('Tom Jones', 5000)

import shelve

db = shelve.open('persondb')
for obj in (bob1, sue1, tom1):
    db[obj.name] = obj
    print("成功")
db.close()

