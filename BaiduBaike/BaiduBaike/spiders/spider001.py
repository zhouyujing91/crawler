#scrapy crawl spider001 -o items.json -t json

#url model: http://baike.baidu.com/view/33668htm

import scrapy

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from BaiduBaike.items import BaidubaikeItem

import urllib
import datetime
import random

class BaidubaikeSpider(scrapy.Spider):
    name = "spider001"
    allowed_domains = ['baike.baidu.com']
    start_urls = [
        'http://baike.baidu.com/fenlei/%E6%94%BF%E6%B2%BB%E4%BA%BA%E7%89%A9',#政治人物
        #'http://baike.baidu.com/fenlei/%E5%8E%86%E5%8F%B2%E4%BA%BA%E7%89%A9',#历史人物
        #'http://baike.baidu.com/fenlei/%E7%BE%8E%E6%9C%AF',#美术
        #'http://baike.baidu.com/fenlei/%E6%88%8F%E5%89%A7',#戏剧
        ]

    content_base_url = 'http://baike.baidu.com'
    catalog_base_url = 'http://baike.baidu.com/fenlei/'


    def parse(self, response):
        sel = scrapy.selector.Selector(response)    
        type = sel.xpath('//div[@class="grid-list grid-list-spot"]/div[@class="clearfix"]/h2/text()').extract()[-1]

        catalog = sel.xpath('//div[@class="grid-list grid-list-spot"]/ul/li')
        for each in catalog:
            item = BaidubaikeItem()
            item['type'] = type
            item['title'] = each.xpath('div[@class="list"]/a[@class="title nslog:7450"]/text()').extract()[-1]
            item['link'] = self.content_base_url + each.xpath('div[@class="list"]/a[@class="title nslog:7450"]/@href').extract()[-1]
            yield Request(item['link'], meta={'item':item} , callback = self.parse_001)

        pages = sel.xpath('//div[@class="page"]/a')
        for each in pages:
            if each.xpath('@id').extract()[-1] == 'next':
                next_page_url = self.catalog_base_url + each.xpath('@href').extract()[-1]
                yield Request(next_page_url, callback = self.parse)



    def parse_001(self, response):
        sel = scrapy.selector.Selector(response)
        item = response.meta['item']
        item['content'] = "hehe"
        item['tag'] = sel.xpath('//span[@class="taglist"]/text()').extract()
        item['path'] = self.get_unique_num()+'.html'
        #urllib.urlretrieve(item['link'],'html/'+item['path'])
        yield item

    def get_unique_num(self):
        nowTime=datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        randomNum=random.randint(0,99)
        if randomNum<=10:  
            randomNum=str(0)+str(randomNum);  
        uniqueNum=str(nowTime)+str(randomNum); 
        return uniqueNum