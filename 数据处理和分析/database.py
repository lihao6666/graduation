import pymongo

class Mongo():
    def __init__(self):
        host = "127.0.0.1"
        port = 27017
        client = pymongo.MongoClient(host,port)
        db = client["parse"]
        self.Weibo = db["Weibo"]  #选择collection
        self.Zhihu = db["Zhihu"]
        self.WeiboHot = db["WeiboHot"]
        self.ZhihuHot = db["ZhihuHot"]
        self.Search = db["Search"]
        self.Analyse_Weibo = db["Analyse_Weibo"]
        self.Analyse_Zhihu = db["Analyse_Zhihu"]
    '''
    版本一，针对第一版本存储
    '''
    # 按照搜索内容和批次读取评论
    # def read_weibos(self,content,patch):
    #     weibos = self.Weibo.find({'search_content':content,"search_patch":patch}).sort([("comments_count",1)])
    #     return weibos

    # # 按照搜索内容和批次读取评论
    # def read_zhihus(self,content,patch):
    #     zhihus = self.Zhihu.find({'search_content':content,"search_patch":patch}).sort([("comments_count",1)])
    #     return zhihus
    '''
    版本二, 针对第二版本存储
    '''
    # 按照搜索内容和批次读取评论
    def read_weibos(self,content,patch):
        weibos = self.Weibo.find_one({'search_content':content,"search_patch":patch})
        return weibos

    # 按照搜索内容和批次读取评论
    def read_zhihus(self,content,patch):
        zhihus = self.Zhihu.find_one({'search_content':content,"search_patch":patch})
        return zhihus

    # 将weibo分析结果写入数据库                            
    def write_weibo(self,weibo):
        self.Analyse_Weibo.insert(weibo)
    # 将zhihu分析结果写入数据库
    def write_zhihu(self,zhihu):
        self.Analyse_Zhihu.insert(zhihu)







