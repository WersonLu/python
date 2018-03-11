#!/usr/bin/env python

# encoding: utf-8

'''
@contact: wersonliugmail.com
@File    : 拉勾改写.py
'''
import requests
import time


class Proxy:

    def __init__(self):
        self.max = 5
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Referer": "https://www.lagou.com/jobs/list_java?px=default&city=%E5%B9%BF%E5%B7%9E",
            "X-Anit-Forge-Code": "0",
            "X-Anit-Forge-Token": "None",
            "X-Requested-With": "XMLHttpRequest"

        }

    def get_page(self, url, data):
        FAILTIME = 0
        try:
            result = requests.post(url, headers=self.headers, data=data)
            result.encoding = "utf-8"
            return result
        except:
            FAILTIME += 1
            if FAILTIME == self.max:
                print("访问错误")


class Job:
    def __init__(self):
        self.datalist = []

    def get_job(self, url, data):
        p = Proxy()
        result = p.get_page(url, data)
        result.encoding = "utf-8"
        result_dict = result.json()
        try:
            job_info = result_dict['content']['positionResult']['result']
            for job in job_info:
                print(job)
            return job_info
        except:
            print("错误")
            return ""


if __name__ == "__main__":
    url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%B9%BF%E5%B7%9E&needAddtionalResult=false&isSchoolJob=0"
    job = Job()
    all_job_info = []
    for x in range(1, 31):
        data = {
            "first": "false",
            "pn": x,
            "kd": "Java"
        }
        current_page_info = job.get_job(url, data)
        all_job_info.extend(current_page_info)
        print("%s爬取" % x)
        time.sleep(3)
