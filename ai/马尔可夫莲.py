#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/5 5:48
 
'''
from urllib.request import urlopen
from random import randint


def wordListSum(wordlist):
    sum = 0
    for word, value in wordlist.items():
        sum += value
    return sum


def retrieveRandomWord(wordlist):
    randIndex = randint(1, wordListSum(wordlist))
    for word, value in wordlist.items():
        randIndex -= value
        if randIndex <= 0:
            return word


def buildWordDict(text):
    # 剔除换行符和引号
    text = text.replace("\n", " ");
    text = text.replace("\"", "");
    # 保证每个标点符号都和前面的单词在一起
    # 这样不会被剔除，保留在马尔可夫链中
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " " + symbol + " ");
    words = text.split(" ")
    # 过滤空单词
    words = [word for word in words if word != ""]
    wordDict = {}
    for i in range(1, len(words)):
        if words[i - 1] not in wordDict:
            # 为单词新建一个词典
            wordDict[words[i - 1]] = {}
        if words[i] not in wordDict[words[i - 1]]:
            wordDict[words[i - 1]][words[i]] = 0
        wordDict[words[i - 1]][words[i]] = wordDict[words[i - 1]][words[i]] + 1
    return wordDict


text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')

wordDict = buildWordDict(text)

length = 100
chain = ""
currentWord = "I"
for i in range(0, length):
    chain += currentWord + ""
    currentWord = retrieveRandomWord(wordDict[currentWord])
    print(chain)
