import scrapy
import sys
import json
from parse.items import WeiboCommentItem,WeiboItem,WeibosItem
from w3lib import html
import time

class WeiboSpider(scrapy.Spider):
    name = 'weibo'
    # allowed_domains = ['https://m.weibo.cn']
    # start_urls = ['https://m.weibo.cn/']
    base_url = "https://m.weibo.cn"
    mid_url = "https://m.weibo.cn/api/container/getindex?"
    weibos_num = 5
    comments_max = 5 #控制评论爬取的轮数，一般一轮20条
    comments_num = 0 #设置当前评论读取轮数
    parser_num = 0
    search_content = "新垣结衣"
    time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    mids = []

    def cookies_dict(self,cookies):
        dict = {}
        for cookie in cookies.split('; '):
            dict[cookie.split('=')[0]]=cookie[cookie.index('=')+1:]
        return dict
    def headers_cookies_set(self):
        self.weibo_cookies = self.cookies_dict(self.settings.get("WEIBO_COOKIES"))
        self.headers = self.settings.get("HEADERS")


    def start_requests(self):
        self.headers_cookies_set()
        yield scrapy.Request(self.base_url,meta = {'content': self.search_content,'headers':self.headers,'mid_url':self.mid_url},callback=self.get_weibo_mid)

    def get_weibo_mid(self, response):
        data = response.json()
        if data["ok"] == 1:
            print("数据读取成功")
            infos = data["data"]["cards"]
            test_count = 0
            for info in infos:
                if test_count < self.weibos_num:
                    self.mids.append(info['mblog']['id'])
                    test_count += 1
                else:
                    break
                # print(info['mblog']['id']) # 读取的id号

        self.comment_urls = [f"{self.base_url}/comments/hotflow?id={mid}&mid={mid}&max_id_type=0" for mid in self.mids]
        self.weibo_urls = [f"{self.base_url}/statuses/extend?id={mid}" for mid in self.mids]
        self.parser_len = len(self.weibo_urls)

        self.weibos = WeibosItem()
        self.weibos["search_content"] = self.search_content
        self.weibos["search_patch"] = 0
        self.weibos["parse_time"] = self.time
        self.weibos["weibos"] = []
        
        yield scrapy.Request(self.weibo_urls[self.parser_num],headers = self.headers,cookies = self.weibo_cookies,callback=self.parse_weibo)
        

    def parse_weibo(self, response):
        print("正在爬取: ",self.weibo_urls[self.parser_num])
        results = json.loads(response.text)
        if results["ok"] == 1:
            self.weibo = WeiboItem()
            # print(results["data"]["longTextContent"])
            # self.weibo["search_content"] = self.search_content
            # self.weibo["search_patch"] = 0
            # self.weibo["parse_time"] = self.time
            self.weibo["mid"] = self.mids[self.parser_num]
            self.weibo["content"] = html.remove_entities(html.remove_tags(results["data"]["longTextContent"]))
            self.weibo["attitudes_count"] = results["data"]["attitudes_count"]
            self.weibo["comments_count"] = results["data"]["comments_count"]
            self.weibo["reposts_count"] = results["data"]["reposts_count"]
            self.weibo["comments"] = []
            # 这里爬取第一条评论url
            print("爬取评论:", self.comment_urls[self.parser_num])
            yield scrapy.Request(self.comment_urls[self.parser_num],headers = self.headers,cookies = self.weibo_cookies,callback=self.parse_comments)
            pass


    def parse_comments(self, response):
        
        results = json.loads(response.text)
        if results["ok"] == 1:
            comments = results["data"]
            max_id = comments["max_id"]
            # print("max_id:",max_id)
            for comment in comments['data']:
                item = WeiboCommentItem()
                item["content"] = html.remove_entities(html.remove_tags((comment["text"])))
                item["like_count"] = comment["like_count"]
                self.weibo["comments"].append(item)
            if self.comments_num < self.comments_max and max_id != 0:
                    self.comments_num += 1
                    s = response.url.find("max_id=")
                    if s >= 0:
                        next_url = response.url.replace(response.url[s:-13],"max_id={}&".format(max_id))
                    else:
                        next_url = ''.join([response.url[0:-13],"max_id={}&max_id_type=0".format(max_id)])
                    # print("下一条评论:",next_url)
                    yield scrapy.Request(next_url,headers = self.headers,cookies = self.weibo_cookies,callback=self.parse_comments)
            else:

                self.comments_num = 0
                self.parser_num += 1
                self.weibos["weibos"].append(self.weibo)
                if self.parser_num < self.parser_len:
                    yield scrapy.Request(self.weibo_urls[self.parser_num],headers = self.headers,cookies = self.weibo_cookies,callback=self.parse_weibo)
                else:
                    yield self.weibos
        else:
            self.comments_num = 0
            self.parser_num += 1
            self.weibos["weibos"].append(self.weibo)
            if self.parser_num < self.parser_len:
                yield scrapy.Request(self.weibo_urls[self.parser_num],headers = self.headers,cookies = self.weibo_cookies,callback=self.parse_weibo)
            else:
                yield self.weibos
        
        


        
