# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from scrapy import Request
import os

class Task2Pipeline(ImagesPipeline):
    def get_media_requests(self, item, info): # setting the image name 
        return [Request(x, meta={'filename': item['image_name']}) for x in item.get(self.images_urls_field, [])]
    

    def file_path(self, request, response=None, info=None): #saving the image with prescribed image name and extension
        image_guid = request.meta.get('filename', '')
        return 'images/%s.jpg' % (image_guid[0])