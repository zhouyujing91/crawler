#scrapy crawl spider002 -o items.json -t json

#url model: http://baike.baidu.com/view/33668


import scrapy

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from BaiduBaike.items import BaidubaikeItem

import urllib
import datetime
import random

class BaidubaikeSpider(scrapy.Spider):
    name = "spider002"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'http://baike.baidu.com/view/0'
        ]

    base_url = 'http://baike.baidu.com/view/'
    
    begin = 0
    end = 100
    index = 0


    def parse(self, response):
        sel = scrapy.selector.Selector(response)    
       
        link = self.base_url + str(self.index)
        if sel.xpath('//div[@id="bd"]/div[@class="errorBox"]').extract() == []:
            item = BaidubaikeItem()
            item['type'] = "hehe"
            item['title'] = str(self.index)
            item['link'] = link
            item['content'] = "hehe"
            item['tag'] = "hehe"
            item['path'] = self.get_unique_num()+'.html'
            yield item

        if self.index < self.end:
            self.index = self.index + 1
            yield Request(self.base_url + str(self.index), callback = self.parse, dont_filter=True)


    def get_unique_num(self):
        nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum=random.randint(0,99)
        if randomNum<=10:  
            randomNum=str(0)+str(randomNum);  
        uniqueNum=str(nowTime)+str(randomNum); 
        return uniqueNum