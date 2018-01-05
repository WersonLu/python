#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2018/1/5 2:09
 
'''
import os
from urllib.request import urlretrieve, urlopen
from bs4 import BeautifulSoup

downloadDirectory = "downloaded"
basUrl = "http://pythonscraping.com"


def getAbsoluteUrl(baseUrl, source):
    if source.startswith("http://www."):
        url = "http://" + source[11:]
    elif source.startswith("http://"):
        url = source
    elif source.startswith("www."):
        url = source[4:]
        url = "http://" + source
    else:
        url = baseUrl + "/" + source
    if baseUrl not in url:
        return None
    return url


def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
    path = absoluteUrl.replece("www", "")
    path = path.replace(baseUrl, "")
    path = downloadDirectory + path
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return path


html = urlopen("http://pythonscraping.com")
bsobj = BeautifulSoup(html)
downloadList = bsobj.find_all(src=True)
for download in downloadList:
    fileUrl = getAbsoluteUrl(basUrl, download["src"])
    if fileUrl is not None:
        print(fileUrl)
urlretrieve(fileUrl, getDownloadPath(basUrl, fileUrl, downloadDirectory))
