# from django.db import models
from djongo import models

# Create your models here.



class WeiboHotItem(models.Model):
    """
    单个微博排名信息
    """
    ranking = models.CharField(verbose_name="排名",max_length = 5)
    content = models.TextField(verbose_name="内容")
    count = models.CharField(verbose_name="热度",max_length = 10)
    desc = models.CharField(verbose_name="热度描述",max_length = 20)

    class Meta:
         abstract = True

    """
    多个排行信息
    """
class WeiboHotsItem(models.Model):

    _id = models.ObjectIdField()   
    time = models.CharField(max_length=20)  
    count = models.IntegerField() #用来记录当前排行计数
    hots = models.ArrayField(model_container = WeiboHotItem) #排行信息

    class Meta:
        verbose_name = "微博排名信息"
        db_table = "WeiboHots"
        get_latest_by = 'time'

class ZhihuHotItem(models.Model):

    """
    单个知乎排名信息
    """
    ranking = models.CharField(verbose_name="排名",max_length = 5)
    content = models.TextField(verbose_name="内容")
    count = models.CharField(verbose_name="热度",max_length = 10)

    class Meta:
         abstract = True

class ZhihuHotsItem(models.Model):
    _id = models.ObjectIdField()
    time = models.CharField(max_length=20)  
    count = models.IntegerField() #用来记录当前排行计数
    hots = models.ArrayField(model_container = ZhihuHotItem) #排行信息

    class Meta:
        verbose_name = "知乎排名信息"
        db_table = "ZhihuHots"

class CountHot(models.Model):
     _id = models.ObjectIdField()
     parse_type = models.CharField(max_length=20)
     count = models.IntegerField() #用来记录当前排行计数

     class Meta:
        verbose_name = "排行计数"
        db_table = "CountHot"



    
class ResCount(models.Model):
    name = models.CharField(max_length = 30) #关键词名称
    value = models.IntegerField() #关键词数目

    class Meta:
         abstract = True

class ResSpirit(models.Model):
    positive = models.IntegerField() #正向情感数目
    negative = models.IntegerField() #负向情感数目

    class Meta:
         abstract = True


class WeiboAnalyseItem(models.Model):
    
    mid = models.CharField(max_length = 20) #微博标识号
    content = models.TextField() # 微博内容
    comments_count = models.IntegerField() # 评论数
    res_count = models.ArrayField(model_container = ResCount) #词频统计结果
    res_spirit = models.EmbeddedField(model_container = ResSpirit) # 情感分析结果

    class Meta:
         abstract = True
    

class WeiboAnalysesItem(models.Model):
    _id = models.ObjectIdField()
    search_content = models.CharField(max_length = 20) # 搜索内容
    search_patch = models.IntegerField()  # 搜索轮次，用于变化查询
    parse_time = models.CharField(max_length = 20) # 爬取时间
    weibos = models.ArrayField(model_container = WeiboAnalyseItem) #多条微博分析结果

    class Meta:
        db_table = "Analyse_Weibo"


class SearchItem(models.Model):
    _id = models.ObjectIdField()
    search_content = models.CharField(max_length = 20) # 搜索内容
    type = models.CharField(max_length = 20)
    patch = models.IntegerField() #当前爬取的批次

    class Meta:
        db_table = "Search"

# class ZhiHuItem(models.Model):
#     search_content = models.IntegerField() # 搜索内容
#     search_patch = models.IntegerField()  # 搜索轮次，用于变化查询
#     parse_time = models.IntegerField() # 爬取时间
#     content = models.IntegerField() # 知乎问题
#     question_id = models.IntegerField()
#     # nice = models.IntegerField() # 点赞数
#     # answers_count = models.IntegerField() # 回答数
#     answers = models.IntegerField() #回答

# class ZhiHuAnswerItem(models.Model):
#     answer_id = models.IntegerField()
#     author_id = models.IntegerField() # 回答者id
#     author_name = models.IntegerField() #回答者名称
#     content = models.IntegerField() # 回答内容
#     voteup_count = models.IntegerField() # 赞同数
#     comment_count = models.IntegerField() # 评论数
#     created_time = models.IntegerField() # 发表时间
#     updated_time = models.IntegerField() #更新时间
#     comments = models.IntegerField()


# class ZhiHuCommentItem(models.Model):
#     comment_id = models.IntegerField() #评论id
#     author_id = models.IntegerField() # 评论者id
#     author_name = models.IntegerField() #评论者名字
#     content = models.IntegerField() # 评论内容
#     vote_count = models.IntegerField() # 赞同数
#     created_time = models.IntegerField()   #发表时间