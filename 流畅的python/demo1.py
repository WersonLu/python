#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com

'''

import collections
from random import choice

"""
namedtuple 来创建一个自定义的tuple对象,并规定其个数,可以用属性(而不是索引)
来引用某个元素,它定义的这个数据类型
有tuple的不可变性,可以根据属性来引用
"""
Card = collections.namedtuple('Card', ['rank', 'suit'])

"""
纸牌类
"""


class FrenchDeck:
    ranks = [str(n) for n in list(range(2, 11)) + list('JQKA')]

    suits = '桃 杏 梅 方'.split()

    def __init__(self):
        # 按花色生成52张牌的列表
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]


beer_card = Card('7', '桃')
print(beer_card)

deck = FrenchDeck()
print(len(deck))
print(deck[0])
print(deck[-1])

print(choice(deck))

print(deck[:3])

print(deck[12::13])

# for card in deck:
#     print(card)

suit_values = dict(桃=3, 杏=2, 梅=1, 方=0)


def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


for card in sorted(deck, key=spades_high):
    print(card)
