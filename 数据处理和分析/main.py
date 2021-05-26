import jieba
from database import Mongo
from snownlp import SnowNLP
from collections import Counter


class Analysis():
    def __init__(self):
        #使用dict保存结果速度快并且便于后面存入数据库
        self.stopwords = [line.strip() for line in open('./static/stop_words/hit_stopwords.txt',encoding='UTF-8').readlines()]
    # comments 为列表传入，功能实现分词和词频统计
    # data为一条微博下的数据
    def analyse(self,data,type):
        if type == "weibo":
            res_weibo = {}
            # res_weibo["search_content"] = data["search_content"]
            # res_weibo["search_patch"] = data["search_patch"]
            # res_weibo["parse_time"] = data["parse_time"]
            res_weibo["mid"] = data["mid"]
            res_weibo["content"] = data["content"]
            res_weibo["comments_count"] = data["comments_count"]
            res_count = self.comments_word_sort(data["comments"]) #分词和词频率
            res_spirit = self.comments_spirit(data["comments"])  #评论的感情色彩
            res_weibo["res_count"] = res_count
            res_weibo["res_spirit"] = res_spirit
            return res_weibo
        elif type == "zhihu":
            pass
            

    # 词频统计，传入的参数为多条评论列表
    def comments_word_sort(self,comments):
        fenci = []
        for comment in comments:
            res = jieba.cut(comment["content"])
            for r in res:
                if r not in self.stopwords and r != ' ':
                    fenci.append(r)
        counter = Counter(fenci)
        mosts = counter.most_common(15)
        res = []
        for most in mosts:
            temp = {}
            temp["name"] = most[0]
            temp["value"] = most[1]
            res.append(temp)
        return res
    # snownlp情感分析，传入的参数为评论列表
    def comments_spirit(self,comments):
        spirits = {}
        for comment in comments:
            scores = 0
            count = 0
            if comment["content"]:
                for sentence in SnowNLP(comment["content"]).sentences:
                    res = SnowNLP(sentence).sentiments
                    scores += res
                    count += 1
                if count > 0:
                    spirits[comment["content"]] = float(format(scores/count,'.2f'))
                else:
                    pass
            else:
                pass
        # print(spirits)
        pos = 0
        neg = 0
        for value in spirits.values():
            # value大于0.5表示积极向，小于0.5表示消极
            if value > 0.5:
                pos += 1
            else:
                neg += 1
        res = {"positive":pos,"negative":neg}

        return res

        
if __name__ == '__main__':
    mongo = Mongo()
    ans = Analysis()
    weibos = mongo.read_weibos(content = "Nike",patch = 1)
    res = {} 
    res["search_content"] = weibos["search_content"]
    res["search_patch"] = weibos["search_patch"]
    res["parse_time"] = weibos["parse_time"]
    res["weibos"] = []
        
    # zhihus = mongo.read_zhihus(content = "Nike",patch = 1)
    for weibo in weibos["weibos"]:
        analyse_res = ans.analyse(weibo,"weibo")
        res["weibos"].append(analyse_res)
    mongo.write_weibo(res)
 
    


    








    



