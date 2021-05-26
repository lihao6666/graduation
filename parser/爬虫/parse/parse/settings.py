# -*- coding: utf-8 -*-

# Scrapy settings for weibo project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'parse'

SPIDER_MODULES = ['parse.spiders']
NEWSPIDER_MODULE = 'parse.spiders'


FEED_EXPORT_ENCODING = 'UTF8'
WEIBO_COOKIES = 'SCF=AtB_JrdWeJmvFuBDcIhoxrdxbOyq91aqB-F7G8_WWePGf44rSQ9gt6lG8SVDvUjI7vEpc_X-PQ-3RKAtIobdykM.; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWJaNizz9qPwJg2SVpavbBs5NHD95QceoMEShn41K-7Ws4DqcjY--8xi--ciKLsi-27i--ci-8Wi-8hi--4iKnfi-zRi--RiK.ciKnXi--RiKy2i-zNi--fiKnNiKn4BH8W; SUB=_2A25NpLyrDeRhGeBM7FAV-CfFzjyIHXVvZsTjrDV6PUJbkdB-LW7AkW1NRNZytRnz3OZzZYQTVAkVfeQAH5o7oM_4; SSOLoginState=1621150971; WEIBOCN_FROM=1110103030; _T_WM=69828366964; XSRF-TOKEN=c963b7; MLOGIN=1; M_WEIBOCN_PARAMS=luicode=10000011&lfid=100103type%3D1%26q%3D%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3&uicode=10000011&fid=100103'
ZHIHU_COOKIES = '_zap=e35071d9-9c31-4ccf-a679-3ea6b887f995; _xsrf=cad73c48-cda4-4200-8944-049822ae48da; d_c0="AOCRcBKjfxGPTtviUcJdGSuA2lBQV_EGyXA=|1593403350"; _ga=GA1.2.614131282.1593403352; l_n_c=1; n_c=1; z_c0="2|1:0|10:1615386714|4:z_c0|92:Mi4xM0ExMkRRQUFBQUFBNEpGd0VxTl9FU1lBQUFCZ0FsVk5XU1kyWVFCd2dWbS0yem5BcVlmTjBrVlhfUTJOMmp4dFZ3|c29f48f3516131d63b1ab47abac318f2eae21bc24e4967ed9981d825aad2e3c5"; q_c1=cbda5a20a5ef4a7d84ca31caaca64128|1615808186000|1596166101000; tst=h; tshl=; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1619413271,1619413323,1619584112,1619749367; SESSIONID=1eL6Px7lRQIGx9ANqYNBn7BpC9Si5LDgNUgIGMCWOpX; JOID=V10WB02UY3bJuyLgWJWwqWntE0dPpQA9_eha0TPFMjmJwRihECTQ_Ki4JOFd2Qvoq3Kr5yYvGKJKQ71coESLEMo=; osd=VV8QAEmWYXDOvyDiXpK0q2vrFENNpwY6-epY1zTBMDuPxhyjEiLX-Kq6IuZZ2wnurHap5SAoHKBIRbpYokaNF84=; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1620030141; KLBRSID=fe78dd346df712f9c4f126150949b853|1620030906|1620030130'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36',
}
MONGO_HOST = '127.0.0.1'
MONGO_PORT = 27017


LOG_LEVEL = "DEBUG"
# LOG_LEVEL = "INFO"
# LOG_ENALBED = False
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'weibo (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#     'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
#     'cookie': 'WEIBOCN_FROM=1110003030; SCF=AtB_JrdWeJmvFuBDcIhoxrdxbOyq91aqB-F7G8_WWePGsWk9z-oklBrwmbW-POonf6xjqZMB9PhkdAMI_8eRElc.; SUB=_2A25NDX67DeRhGeBM7FAV-CfFzjyIHXVuDgLzrDV6PUJbktANLUb-kW1NRNZytRir39dz3xqz05hLrw_RvyiO7OMX; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WWJaNizz9qPwJg2SVpavbBs5NHD95QceoMEShn41K-7Ws4DqcjY--8xi--ciKLsi-27i--ci-8Wi-8hi--4iKnfi-zRi--RiK.ciKnXi--RiKy2i-zNi--fiKnNiKn4BH8W; SSOLoginState=1611206379'
# }

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'weibo.middlewares.WeiboSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'parse.middlewares.WeiboDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'parse.pipelines.SpiderPipeline': 300,
#    'weibo.pipelines.ZhihuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
