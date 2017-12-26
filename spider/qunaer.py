#!/usr/bin/env python

# encoding: utf-8

'''
 
@author: wersonliu

@contact: wersonliugmail.com
 
@time: 2017/12/22 16:17
 
'''
# 去哪儿酒店 模拟浏览器爬取
import codecs
import datetime
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time


class QunaSpider(object):

    def get_hotel(self, driver, to_city, fromdate, todate):
        ele_toCity = driver.find_element_by_name('toCity')  # 目的地城市 name为"tocity"
        ele_fromDate = driver.find_element_by_id('fromDate')  # 入住时间 id为fromdate
        ele_toDate = driver.find_element_by_id('toDate')  # 离开时间
        # ele_search = driver.find_element_by_name('search-button')
        # 搜索按钮
        ele_search = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div/div[2]/form[1]/div[3]/div[1]/a')

        ele_toCity.clear()  # 为什么要清除?
        ele_toCity.send_keys(to_city)  # 把to_city传入 ele_toCity这个取到的框
        ele_toCity.click()  # 点击这个框,填入操作
        ele_fromDate.clear()  # 清除入住框的其他信息
        ele_fromDate.send_keys(fromdate)  # 把入住时间传入取到的框
        ele_toDate.clear()  # 清除离开框的其他信息
        ele_toDate.send_keys(todate)  # 离开时间填入
        ele_search.click()  # 点击搜索框
        page_num = 0
        while True:
            try:
                # 显示等待(条件触发式), 如果页面没有找到这个to_city字符内容就抛异常
                WebDriverWait(driver, 10).until(EC.title_contains(str(to_city)))
            except Exception as e:
                print(e)
                break
            # 等待5秒,模拟鼠标滚动到下面加载更多
            time.sleep(5)
            # 模拟滚动的js代码
            js = "window.scrollTo(0,document.body.scrollHeight);"
            driver.execute_script(js)
            time.sleep(5)

            htm_const = driver.page_source  # 取得网页内容
            soup = BeautifulSoup(htm_const, 'html.parser', from_encoding='utf-8')
            infos = soup.find_all(class_="item_hotel_info")  # 找到包含酒店信息的div块
            f = codecs.open("qunae.txt", 'a', 'utf-8')  # 以追加模式打开新建一个文件

            for info in infos:
                # 先写入页码标识
                f.write(str(page_num) + '--' * 10)
                # 去除首位空格换行符
                content = info.get_text().replace(" ", "").replace("\t", "").strip()

                for line in [In for In in content.splitlines() if In.strip()]:
                    f.write(line)
                    f.write('\r\n')
            f.close()
            try:
                # 找打下一页这个div
                next_page = WebDriverWait(driver, 10).until(
                    EC.visibility_of(driver.find_element_by_css_selector(".item.next")))
                # 点击它
                next_page.click()
                # 同时page_num参数加1
                page_num += 1
                # 等待10秒
                time.sleep(10)
            except Exception as e:
                print(e)
                break

    # 参数为路径,目的地
    def crawl(self, root_url, to_city):
        # 以系统时间转为日期并附带格式
        today = datetime.date.today().strftime('%Y-%m-%d')
        tomorrow = datetime.date.today() + datetime.timedelta(days=1)
        tomorrow = tomorrow.strftime('%Y-%m-%d')
        driver = webdriver.Firefox(executable_path='D:\Anaconda3\geckodriver.exe')
        # 设置页面加载时间
        driver.set_page_load_timeout(50)
        # 加载这个url路径
        driver.get(root_url)
        # 窗口最大化
        driver.maximize_window()
        # 显式等待
        driver.implicitly_wait(10)
        # 带入参数执行上面的方法
        self.get_hotel(driver, to_city, today, tomorrow)


if __name__ == "__main__":
    # 实例化这个对象
    spider = QunaSpider()
    # 调用里面的方法
    spider.crawl('http://hotel.qunar.com/', u"上海")
