#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 校车的故事(深浅拷贝).py
'''

import copy


class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)

    # 上车
    def pick(self, name):
        self.passengers.append(name)

    # 下车
    def drop(self, name):
        self.passengers.remove(name)


bus1 = Bus(['刘伟', '成立', '成龙', '周杰伦'])
bus2 = copy.copy(bus1)
bus4 = Bus()
print(bus4.passengers)  # []
print("...")
bus3 = copy.deepcopy(bus1)
print(id(bus1), id(bus2), id(bus3))
# 80973776 81004240 81005488
bus1.drop('刘伟')
print(bus1.passengers)
print(bus2.passengers)
print(bus3.passengers)
# ['成立', '成龙', '周杰伦']
# ['成立', '成龙', '周杰伦']
# ['刘伟', '成立', '成龙', '周杰伦']
