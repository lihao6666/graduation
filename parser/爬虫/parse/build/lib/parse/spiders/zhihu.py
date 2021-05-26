import scrapy
import requests
import execjs
import hashlib
from parse.items import ZhiHuItem,ZhiHuAnswerItem,ZhiHuCommentItem
from w3lib import html
import time
import urllib
# tupTime = time.localtime(1566366555)#秒时间戳
# stadardTime = time.strftime("%Y-%m-%d %H:%M:%S", tupTime)
# print(stadardTime)
# #2019-08-21 13:49:15

class ZhihuSpider(scrapy.Spider):
    name = 'zhihu'
    search_content = "Nike"
    start_url = 'https://www.zhihu.com/api/v4/search_v3?t=general&q={search}&correction=1&offset=0&limit=20&lc_idx=0&show_all_topics=0'.format(search = search_content)
    referer = "https://www.zhihu.com/search?type=content&q=%{search}".format(search = search_content)
    # answer_url = "https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=content&limit=20&offset=0&sort_by=default"
    answer_url = "https://www.zhihu.com/api/v4/questions/{question_id}/answers?include=data%5B*%5D.is_normal%2Ccontent%2Ccomment_count%2Cvoteup_count%2Cexcerpt&limit=20&offset=0&sort_by=default"
    comment_url = "https://www.zhihu.com/api/v4/answers/{answer_id}/root_comments?order=normal&limit=20&offset=0&status=open"
    question_count = 5 #问题数
    answer_count = 5 # 回答数
    comment_count = 20 # 回答下的评论数
    cout_count = 0 #统计yield数据的标记
    prior_max = 30 #设置最多爬取answer_count上限
    time = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())



    def cookies_dict(self,cookies):
        dict = {}
        for cookie in cookies.split('; '):
            dict[cookie.split('=')[0]]=cookie[cookie.index('=')+1:]
        return dict

    def cookies_set(self):
        self.zhihu_cookies = self.cookies_dict(self.settings.get("ZHIHU_COOKIES"))

    def headers_set(self, mode):
        d_c0 = self.zhihu_cookies['d_c0']
        search_encode = urllib.parse.quote(self.search_content)
        url = "/api/v4/search_v3?t=general&q={search}&correction=1&offset=0&limit=20&lc_idx=0&show_all_topics=0".format(search = search_encode)
        # url = "/api/v4/search_v3?t=general&q=%E5%8D%B0%E5%BA%A6&correction=1&offset=0&limit=20&lc_idx=0&show_all_topics=0"
        if mode == 1:
            f = "+".join(["3_2.0", url, d_c0,"undefined"]) 
        else:
            f = "+".join(["3_2.0", url, d_c0]) 
        print(f)
        fmd5 = hashlib.new('md5', f.encode()).hexdigest()
        with open('./static/g_encrypt.js', 'r') as f:
            ctx1 = execjs.compile(f.read(), cwd=r'/usr/local/lib/node_modules')
        encrypt_str = ctx1.call('b', fmd5)
        print(encrypt_str)

        self.headers =  {
            "referer": self.referer,	
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            "x-api-version": "3.0.91",
            "x-zse-83": "3_2.0",
            "x-zse-86": "2.0_%s" % encrypt_str,
        }
        self.headers2 =  {
            # "referer": self.referer,	
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
            # "x-api-version": "3.0.91",
            # "x-zse-83": "3_2.0",
            # "x-zse-86": "2.0_%s" % encrypt_str,
        }
        if mode == 1:
            self.headers["x-zst-81"] = "undefined"
        # res = requests.get(self.start_url,headers = self.headers,cookies = self.zhihu_cookies)
        # pass
    def start_requests(self):
        self.cookies_set()
        self.headers_set(0)
        # print(self.headers)
        yield scrapy.Request(self.start_url,headers = self.headers,cookies = self.zhihu_cookies,callback=self.parse_zhihu)

    def parse_zhihu(self, response):
        res = response.json()
        datas = res["data"]
        self.zhihus = []
        count = 0
        for data in datas:
            if count < self.question_count:
                if data["type"] == "search_result":
                    zhihu = ZhiHuItem()
                    question = data["object"].get("question")
                    # print(question)
                    if question:
                        zhihu["search_content"] = self.search_content
                        zhihu["search_patch"] = 0
                        zhihu["parse_time"] = self.time
                        zhihu["question_id"] = question["id"]
                        zhihu["content"] = html.remove_entities(html.remove_tags(question["name"]))
                        zhihu["answers"] = []
                        self.zhihus.append(zhihu)
                        count += 1
                        print("question_id: ",zhihu["question_id"])
                    # 爬取相关内容的知乎问题包括id
                        yield scrapy.Request(self.answer_url.format(question_id=zhihu["question_id"]),headers = self.headers2,cookies = self.zhihu_cookies,meta = {'question' : zhihu,'count_question': count},callback=self.parse_answer)
            else:
                break
        # for zhihu in self.zhihus:
        #     yield zhihu
        # yield self.zhihus
    def parse_answer(self, response):
        res = response.json()
        datas = res["data"]
        # question = response.meta['question']
        count_question = response.meta['count_question']
        count_answer = 0
        answer_len = len(datas)
        # print("answer_count: ",answer_len)   
        # answers = []
        for data in datas:
            if count_answer < self.answer_count:
                answer = ZhiHuAnswerItem()
                answer["answer_id"] = data["id"]
                author = data.get("author")
                if author:
                    answer["author_id"] = author["id"]
                    answer["author_name"] = author["name"]
                else:
                    answer["author_id"] = "无"
                    answer["author_name"] = "无"
                answer["content"] = html.remove_entities(html.remove_tags(data["excerpt"]))
                answer["voteup_count"] = data["voteup_count"]
                answer["comment_count"] = data["comment_count"]
                answer["created_time"] = data["created_time"]
                answer["updated_time"] = data["updated_time"]
                answer["comments"] = []
                count_answer += 1
                # print("prior:",self.prior_max-count_answer)
                # print("answer_id:",count_answer)
                # answers.append(answer)
                yield scrapy.Request(self.comment_url.format(answer_id=answer["answer_id"]),headers = self.headers2,cookies = self.zhihu_cookies,meta = {'count_question' : count_question,'answer': answer,'count_answer': count_answer,'answer_len': answer_len},callback=self.parse_comment)
        # self.zhihus[count_question]["answers"] = answers
        # if count == self.question_count:
        #     for zhihu in self.zhihus:
        #         yield zhihu
        
    def parse_comment(self, response):
        self.cout_count += 1
        res = response.json()
        datas = res["data"]
        count_question = response.meta['count_question']
        answer = response.meta['answer']
        count_answer = response.meta['count_answer']
        answer_len = response.meta['answer_len']
        count_comment = 0
        comments = []
        # print("comment_count: ",len(datas))
        for data in datas:
            if count_comment < self.comment_count:
                comment = ZhiHuCommentItem()
                comment["comment_id"] = data["id"]
                author = data["author"]["member"]
                if author:
                    comment["author_id"] = author["id"]
                    comment["author_name"] = author["name"]
                else:
                    comment["author_id"] = "无"
                    comment["author_name"] = "无"
                comment["content"] = html.remove_entities(html.remove_tags(data["content"]))
                comment["vote_count"] = data["vote_count"]
                comment["created_time"] = data["created_time"]
                count_comment += 1
                comments.append(comment)
        
        answer["comments"] = comments
        self.zhihus[count_question-1]["answers"].append(answer)
        # print("count_answer:" count_answer)
        if self.cout_count == answer_len or self.cout_count == self.answer_count:
            self.cout_count = 0
            yield self.zhihus[count_question-1]
        
        # if count_question == self.question_count:
        #     for zhihu in self.zhihus:
        #         yield zhihu
    