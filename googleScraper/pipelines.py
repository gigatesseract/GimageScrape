# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.http.request import Request

from scrapy.pipelines.images import ImagesPipeline


class GooglescraperPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item["url"], meta={"image_name": item["name"]})

    def file_path(self, request, response=None, info=None):
        return "%s/%s.jpg" % (
            request.meta["image_name"].split("_")[0],
            request.meta["image_name"].split("_")[1],
        )

    def item_completed(self, results, item, info):
        print("\n\nentered into item_completed\n")
        print("Name : ", item["name"])
        print("Results:", results)
