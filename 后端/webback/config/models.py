# from django.db import models
from djongo import models
# Create your models here.



class ConfigMes(models.Model):
    """
    爬虫的一些配置信息
    """
    _id = models.ObjectIdField()
    parse_type = models.CharField(max_length=20, verbose_name='爬虫类别') # 可以是zhihu或者weibo
    headers = models.TextField(verbose_name='请求头headers')
    cookies = models.TextField(verbose_name='cookies')
    status = models.CharField(max_length = 20)

    class Meta:
        verbose_name = "配置信息"
        db_table = "Config"

# class Users(models.Model):
#     """
#     自定义用户信息
#     """
#     user_id = models.CharField(max_length=20, verbose_name='用户id')
#     password = models.CharField(max_length=30, verbose_name='用户密码')
    

#     class Meta:
#         verbose_name = "用户信息"
