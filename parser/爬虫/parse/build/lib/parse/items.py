# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class WeiboHots(scrapy.Item):
    parse_type = scrapy.Field()
    hots = scrapy.Field()
    
class ZhihuHots(scrapy.Item):
    parse_type = scrapy.Field()
    hots = scrapy.Field()

class WeibosItem(scrapy.Item):
    search_content = scrapy.Field() # 搜索内容
    search_patch = scrapy.Field()  # 搜索轮次，用于变化查询
    parse_time = scrapy.Field() # 爬取时间
    weibos = scrapy.Field() #微博

class WeiboTopItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    ranking = scrapy.Field()
    content = scrapy.Field()
    count = scrapy.Field()
    desc = scrapy.Field()

class ZhiHuTopItem(scrapy.Item):
    ranking = scrapy.Field()
    content = scrapy.Field()
    count = scrapy.Field()
    
class WeiboItem(scrapy.Item):
    # search_content = scrapy.Field() # 搜索内容
    # search_patch = scrapy.Field()  # 搜索轮次，用于变化查询
    # parse_time = scrapy.Field() # 爬取时间
    
    mid = scrapy.Field() #微博标识号
    content = scrapy.Field() # 微博内容
    attitudes_count = scrapy.Field() #点赞数
    comments_count = scrapy.Field() # 评论数
    reposts_count = scrapy.Field() # 转发数
    comments = scrapy.Field() #评论

class WeiboCommentItem(scrapy.Item):
    content = scrapy.Field()
    like_count = scrapy.Field()

class ZhiHuItem(scrapy.Item):
    search_content = scrapy.Field() # 搜索内容
    search_patch = scrapy.Field()  # 搜索轮次，用于变化查询
    parse_time = scrapy.Field() # 爬取时间
    content = scrapy.Field() # 知乎问题
    question_id = scrapy.Field()
    # nice = scrapy.Field() # 点赞数
    # answers_count = scrapy.Field() # 回答数
    answers = scrapy.Field() #回答

class ZhiHuAnswerItem(scrapy.Item):
    answer_id = scrapy.Field()
    author_id = scrapy.Field() # 回答者id
    author_name = scrapy.Field() #回答者名称
    content = scrapy.Field() # 回答内容
    voteup_count = scrapy.Field() # 赞同数
    comment_count = scrapy.Field() # 评论数
    created_time = scrapy.Field() # 发表时间
    updated_time = scrapy.Field() #更新时间
    comments = scrapy.Field()


class ZhiHuCommentItem(scrapy.Item):
    comment_id = scrapy.Field() #评论id
    author_id = scrapy.Field() # 评论者id
    author_name = scrapy.Field() #评论者名字
    content = scrapy.Field() # 评论内容
    vote_count = scrapy.Field() # 赞同数
    created_time = scrapy.Field()   #发表时间
    

