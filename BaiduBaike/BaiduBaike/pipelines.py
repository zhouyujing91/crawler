# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import urllib
import json  
import codecs  


class BaidubaikePipeline(object):
    #def __init__(self):  
    #    self.file = codecs.open('baidubaike_items_utf8.json', 'wb', encoding='utf-8')  

    def process_item(self, item, spider):

        #line = json.dumps(dict(item)) + '\n'
        #self.file.write(line.decode("unicode_escape")) 

        urllib.urlretrieve(item['link'],'html/'+item['path'])

        return item
