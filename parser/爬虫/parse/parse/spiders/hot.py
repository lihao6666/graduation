import scrapy
from parse.items import WeiboTopItem,ZhiHuTopItem,WeiboHots,ZhihuHots


class HotSpider(scrapy.Spider):
    name = 'hot'
    # allowed_domains = ['https://s.weibo.com/top/summary/']
    start_url = 'https://s.weibo.com/top/summary/'
    next_url = 'https://www.zhihu.com/hot'

    def cookies_dict(self,cookies):
        dict = {}
        for cookie in cookies.split('; '):
            dict[cookie.split('=')[0]]=cookie[cookie.index('=')+1:]
        return dict
    def headers_cookies_set(self):
        self.weibo_cookies = self.cookies_dict(self.settings.get("WEIBO_COOKIES"))
        self.zhihu_cookies = self.cookies_dict(self.settings.get("ZHIHU_COOKIES"))
        self.headers = self.settings.get("HEADERS")
        
        
    def start_requests(self):
        print(self.desc)
        self.headers_cookies_set()
        yield scrapy.Request(self.start_url,headers = self.headers,cookies = self.weibo_cookies,callback=self.parse_weibo)
    def parse_weibo(self, response):
        weibo_hots = WeiboHots()
        hots_res = []
        try:
            hots = response.xpath("//tr")
            for hot in hots:
                item = WeiboTopItem()
                item['ranking'] = hot.xpath('td[@class="td-01 ranktop"]/text()').get()
                item['content'] = hot.xpath('td[@class="td-02"]/a/text()').extract_first()
                item['count'] = hot.xpath('td[@class="td-02"]/span/text()').extract_first()
                item['desc'] = hot.xpath('td[@class="td-03"]/i/text()').extract_first()
                if not item['ranking']:
                    pass
                else:
                    hots_res.append(item)

        except:
            print("出错了")
            return
        else:
            weibo_hots['parse_type'] = "weibo"
            weibo_hots['hots'] = hots_res
            yield weibo_hots
            yield scrapy.Request(self.next_url,headers = self.headers,cookies = self.zhihu_cookies,callback=self.parse_zhihu)

    def parse_zhihu(self, response):
        zhihu_hots = ZhihuHots()
        hots_res = []
        hots = response.xpath('//section')

        for hot in hots:
            item = ZhiHuTopItem()

            item['ranking'] = hot.xpath('div[@class="HotItem-index"]/div/text()').get()
            item['content'] = hot.xpath('div[@class="HotItem-content"]/a/h2/text()').extract_first()
            item['count'] = hot.xpath('div[@class="HotItem-content"]/div/text()').extract_first()
            hots_res.append(item)
        zhihu_hots['parse_type'] = "zhihu"
        zhihu_hots['hots'] = hots_res
        yield zhihu_hots

