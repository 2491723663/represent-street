import scrapy
from selenium import webdriver
from Amazon_su.items import AmazontestItem
import time
import sys
import os
import re


class AmazonSpider(scrapy.Spider):
    name = 'Amazon'
    # allowed_domains = ['www.xxx.com']
    # start_urls = ['https://www.amazon.com/s?k=80cc&i=automotive&page=1']
    start_url = 'https://www.amazon.com/s?k=80cc&i=automotive&page=1'

    url = 'https://www.amazon.com/s?k=80cc&i=automotive&page=%d'

    page_num = 2

    def __init__(self):

        # 计算耗时
        self.start_time = time.perf_counter()

    def start_requests(self):
        yield scrapy.Request(url=self.start_url, callback=self.parse)

    def parse(self, response):
        # name = response.xpath('//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[3]/div/span/div/div/div/div/div[2]/h2/a/span/text()').extract_first()
        div_list = response.xpath('//div[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div')
        if div_list == None:
            print('出错了')
        for div in div_list[2:35]:
            item = AmazontestItem()
            asin = div.xpath('./@data-asin')[0].extract()
            url = div.xpath('.//h2/a/@href ')[0].extract()
            item['asin'] = asin

            new_url = 'https://www.amazon.com/' + url
            item['url'] = new_url

            yield scrapy.Request(new_url, callback=self.parse_url, meta={'item': item})

        # 分页
        # if (self.page_num <= 2):
        #     new_url = format(self.url % self.page_num)
        #     self.page_num += 1
        #     yield scrapy.Request(url=new_url, callback=self.parse)



    def parse_url(self, response):

        item = response.meta['item']
        print(item['url'])
        page_text = response.text

        #通过正则表达式解析数据
        pattern_big = re.compile('#(.*?\sin[A-Za-z &]+)\(')
        item_big = re.findall(pattern_big, page_text)
        if item_big!=None:
            item["rank_big"] = " ".join(item_big)
            print(" ".join(item_big))

        pattern_small = re.compile("#(.*?\sin ).*?'>([A-Za-z &]+)</a>")
        items_small = re.findall(pattern_small, page_text)

        list = []
        if items_small != None:
            for item_small in items_small:
                list.append(item_small[0] + item_small[1])
            item["rank_small"] = ";".join(list)
            print(";".join(list))
        item["cookie"] =  response.request.headers.getlist('cookie')

        yield item


        # 统计耗时
        stop_time = time.perf_counter()

        cost = stop_time - self.start_time

        print("%s cost %s second" % (os.path.basename(sys.argv[0]), cost))

    # def close(self, spider):
    #     self.bro.quit()