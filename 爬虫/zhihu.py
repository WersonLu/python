#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/27 1:48
 
'''
from selenium import webdriver
import time
import urllib.request
from bs4 import BeautifulSoup
import html.parser
import random

def main(url):

    driver = webdriver.Chrome()  # 打开浏览器

    # 列出来你想要下载图片的网站
    # driver.get("https://www.zhihu.com/question/35931586") # 你的日常搭配是什么样子？
    # driver.get("https://www.zhihu.com/question/61235373") # 女生腿好看胸平是一种什么体验？
    # driver.get("https://www.zhihu.com/question/28481779") # 腿长是一种什么体验？
    # driver.get("https://www.zhihu.com/question/19671417") # 拍照时怎样摆姿势好看？
    # driver.get("https://www.zhihu.com/question/20196263") # 女性胸部过大会有哪些困扰与不便？
    # driver.get("https://www.zhihu.com/question/46458423") # 短发女孩要怎么拍照才性感？
    # urls = ["https://www.zhihu.com/question/35931586", "https://www.zhihu.com/question/61235373",
    #         "https://www.zhihu.com/question/28481779", "https://www.zhihu.com/question/19671417",
    #         "https://www.zhihu.com/question/46458423"]
    driver.get(url)

    # 假装点击更多按钮的次数
    def execute_times(times):

        for i in range(times):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            try:
                driver.find_element_by_css_selector('button.QuestionMainAction').click()
                print("page" + str(i))
                time.sleep(1)
            except:
                break

    execute_times(5)

    # 这是原网页 HTML 信息
    result_raw = driver.page_source
    # 以这个规则解析
    result_soup = BeautifulSoup(result_raw, 'html.parser')
    # 结构化原 HTML 文件
    result_bf = result_soup.prettify()
    # 可写可不写
    with open("raw_result.txt", 'w', encoding='utf-8') as girls:
        girls.write(result_bf)
    girls.close()
    print("原网页信息保存成功!!!")

    # ****************   Find all <nonscript> nodes and store them   *****************************************
    with open("noscript_meta.txt", 'w') as noscript_meta:
        noscript_nodes = result_soup.find_all('noscript')  # 找到所有<noscript>node
        noscript_inner_all = ""
        for noscript in noscript_nodes:
            noscript_inner = noscript.get_text()  # 获取<noscript>node内部内容
            noscript_inner_all += noscript_inner + "\n"

        noscript_all = html.parser.unescape(noscript_inner_all)  # 将内部内容转码并存储
        noscript_meta.write(noscript_all)

    noscript_meta.close()
    print(" noscript标签保存成功!!!")

    # ****************   Store meta data of imgs  *****************************************
    img_soup = BeautifulSoup(noscript_all, 'html.parser')
    img_nodes = img_soup.find_all('img')
    with open("img_meta.txt", 'w') as img_meta:
        count = 0
        for img in img_nodes:
            # src属性不为空取出来
            if img.get('src') is not None:
                img_url = img.get('src')

                line = str(count) + "\t" + img_url + "\n"
                img_meta.write(line)
                # 下载
                urllib.request.urlretrieve(img_url, "E:\\数据文件\\图片\\" + str(random.random()) + ".jpg")  # 一个一个下载图片
                count += 1

    img_meta.close()
    print("图片下载成功")


if __name__ == '__main__':
    urls = ["https://www.zhihu.com/question/35931586", "https://www.zhihu.com/question/61235373",
            "https://www.zhihu.com/question/28481779", "https://www.zhihu.com/question/19671417",
            "https://www.zhihu.com/question/46458423"]
    for url in urls:
        time.sleep(2)
        main(url)
