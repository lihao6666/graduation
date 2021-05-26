# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import time
from pymongo.errors import DuplicateKeyError
from scrapy.utils.project import get_project_settings
# from settings import MONGO_HOST, MONGO_PORT
# from parse.items import WeiboTopItem,WeiboItem,WeiboCommentItem,ZhiHuTopItem,ZhiHuItem,ZhiHuAnswerItem,ZhiHuCommentItem


# class WeiboPipeline(object):
#     def process_item(self, item, spider):
#         return item

class SpiderPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        client = pymongo.MongoClient(settings.get("MONGO_HOST"), settings.get("MONGO_PORT"))
        self.db = client['parse'] # 选择数据库
        self.set = False #设置第几轮读取
        self.time = time.strftime("%Y-%m-%d %H:00",time.localtime())
    # 读取当前爬取批次
    def set_patch(self,type):
        search = self.Search.find_one({"search_content":self.search_content,"type":type})
        if search:
            self.patch = search["patch"]+1
            self.Search.update_one({"search_content":self.search_content},{"$set": { "patch": self.patch }})
        else:
            self.patch = 1
            self.insert_item(self.Search,{"search_content":self.search_content,"type":type,"patch":1})
        self.set = True
    # 启动爬虫之前
    def open_spider(self,spider):
        if spider.name == "hot":
            spider.desc = "res"
            self.WeiboHot = self.db["WeiboHots"]
            self.ZhihuHot = self.db["ZhihuHots"]
            self.CountHot = self.db["CountHot"]
            # self.zhihu_hots = []
            # self.weibo_hots = []
            weibo_doc = {"parse_type":"weibo"}
            zhihu_doc = {"parse_type":"zhihu"}
            weibo_hot = self.CountHot.find_one(weibo_doc) #找到weibo热榜的数目
            zhihu_hot = self.CountHot.find_one(zhihu_doc) #找到知乎热榜的数目
            self.weibo_new_count = weibo_hot["count"] + 1
            self.zhihu_new_count = zhihu_hot["count"] + 1
            self.CountHot.update_one(weibo_doc,{"$set": { "count": self.weibo_new_count}}) #更新数据库中热榜数目
            self.CountHot.update_one(zhihu_doc,{"$set": { "count": self.zhihu_new_count}})

            # self.WeiboHot.remove({}) #数据库表清空
            # self.ZhihuHot.remove({})
        elif spider.name == "weibo":
            self.Weibo = self.db["Weibo"]
            self.Search = self.db["Search"]

        else:
            self.Zhihu = self.db["Zhihu"]
            self.Search = self.db["Search"]


    def close_spider(self,spider):
        pass


    # 爬虫处理
    def process_item(self, item, spider):
        # print(spider.name)
        if spider.name == 'hot':
            if item["parse_type"] == "weibo":
                hot = {}
                hot["time"] = self.time 
                hot["count"] = self.weibo_new_count
                hot["hots"] = item["hots"]
                self.insert_item(self.WeiboHot, hot)
            elif item["parse_type"] == "zhihu":
                hot = {}
                hot["time"] = self.time 
                hot["count"] = self.zhihu_new_count
                hot["hots"] = item["hots"]
                self.insert_item(self.ZhihuHot, hot)
        elif spider.name == 'zhihu' or spider.name == 'weibo':
            # print(item["content"])
            if not self.set:
                self.search_content = item["search_content"]
                self.set_patch(spider.name)
            else:
                pass
            item["search_patch"] = self.patch
            if spider.name == "zhihu":
                self.insert_item(self.Zhihu, item)
            elif spider.name == "weibo":
                self.insert_item(self.Weibo, item)
        return item

    @staticmethod
    def insert_item(collection, item):
        try:
            collection.insert(dict(item))
        except DuplicateKeyError:
            print("pipe error")
            pass
    
    