# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import requests
from scrapy.http import HtmlResponse


class WeiboSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class WeiboDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    def __init__(self, ):
        chrome_options= webdriver.ChromeOptions()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        mobileEmulation = {'deviceName' :'iPhone 6'}
        chrome_options.add_experimental_option('mobileEmulation',mobileEmulation)
        self.browser = webdriver.Chrome(chrome_options=chrome_options)
        # browser.set_window_size(1920, 1080)
        self.wait = WebDriverWait(self.browser,2)

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        if request.meta.get('mid_url'):
            self.content = request.meta.get('content')
            self.headers = request.meta.get('headers')
            self.mid_url = request.meta.get('mid_url')
            
            self.browser.get(request.url)
            self.browser.find_element_by_class_name('m-search').click()
            input = self.wait.until(EC.presence_of_element_located((By.XPATH, '//input')))
            input.send_keys(self.content)
            input.send_keys(Keys.ENTER)
            # self.wait.until(EC.presence_of_element_located((By.XPATH,'//li/span[contains(text(),"热门")]'))).click()
            more = self.wait.until(EC.presence_of_element_located((By.XPATH,'//*[contains(text(),"更多热门微博")]')))
            self.browser.execute_script("arguments[0].click()",more)
            sp = self.browser.current_url.find("index")
            self.target_url = self.mid_url+self.browser.current_url[sp+6:-1]
            # print(self.target_url)
            self.browser.quit()


            response = requests.get(url=self.target_url,headers = self.headers)


            return HtmlResponse(url = self.target_url,body=response.text,encoding="utf-8",request=request,status=200)
        else:
            return None
            #这里返回的是Noned的时候，spider会继续访问Request

        
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
