# -*- coding: utf-8 -*-
import scrapy
import re

from scrapy import Request

from sz_house.items import SzHouseItem


class ZdHouseSpider(scrapy.Spider):
    name = 'zd_house'
    allowed_domains = ['sz.lianjia.com/ershoufang/']
    start_urls = ['http://sz.lianjia.com/ershoufang//']

    def parse(self, response):
        # / html / body / div[4] / div[1] / ul / li[1]
        clears = response.css('.sellListContent li')

        for c in clears:
            item = SzHouseItem()
            try:
                house = c.css('.houseInfo a::text').extract_first()
                house_text = c.css('.houseInfo::text').extract_first()
                house_info_list = [e for e in re.split('\|', house_text) if len(e) > 1]
                house_room = house_info_list[0].strip()
                # 面积
                house_area = ''.join(re.findall(r'[\d+\.]', house_info_list[1]))

                total_price = c.css('.totalPrice span::text').extract_first()

                unit_price = c.css('.unitPrice span::text').extract_first()

                unit_price = re.findall('\d+', unit_price)[0]

                # area = house.xpath("./div[@class=info]/div[@class=flood]/div[@class=positionInfo]/a/text()").extract_first()
                # totalPrice = house.xpath(
                #     "./div[@class=info]/div[@class=priceInfo]/div[@class=totalPrice]/span/text()").extract_first()
                # unitPrice = house.xpath(
                #     "./div[@class=info]/div[@class=priceInfo]/div[@class=unitPrice]/span/text()").extract_first()
                item['house'] = house
                item['total_price'] = float(total_price)
                item['unit_price'] = float(unit_price)
                item['house_area'] = float(house_area)
                item['house_room'] = house_room

                yield item

                # 翻页
                page_info = response.css('div[class="page-box fr"]'). \
                    css('div::attr(page-data)').extract_first()

                # 取出这个页码总数
                page_list = re.findall('\d+', page_info)

                next_page = 'pg' + str(int(page_list[1]) + 1)
                # 构造url
                url = self.start_urls[0] + next_page
                # 再次提交请求
                yield Request(url=url, callback=self.parse)



            except Exception as e:

                print(e, house_info_list)
