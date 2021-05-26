from django.shortcuts import render
from django.views import View
import json
from parse import models
from django import http
from django.core import serializers
from django.forms.models import model_to_dict
from bson import ObjectId
# Create your views here.

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o,ObjectId):
            return str(o)
        return json.JSONEncoder.default(self,o)

class HotView(View):
    def get(self, request):
        # json_data = json.loads(self.request.body.decode("utf-8"))
        # hot_type = json_data["hot_type"]
        hot_type = request.GET.get("hot_type")
        count = int(request.GET.get("count"))

        if count == -1:
            if hot_type == "weibo":
                count = models.CountHot.objects.get(parse_type = "weibo").count
                print(count)
                res = models.WeiboHotsItem.objects.filter(count=count)
            elif hot_type == "zhihu":
                count = models.CountHot.objects.get(parse_type = "zhihu").count
                res = models.ZhihuHotsItem.objects.filter(count=count)
        else:
            if hot_type == "weibo":
                res = models.WeiboHotsItem.objects.filter(count=count)
            elif hot_type == "zhihu":
                res = models.ZhihuHotsItem.objects.filter(count=count)

        # print(res)
        # hots = res.values()[0].get('hots')
        hots = serializers.serialize("json",res,ensure_ascii = False) #最强改bug
        hots = json.loads(hots)
        res = json.loads(hots[0].get("fields")["hots"])
        hots[0]["fields"]["hots"] = res
        # print(hots)
        

        return http.JsonResponse(hots[0] ,safe = False, status = 200)
class HotChangeView(View):
    def get(self, request):
        date = request.GET.get("date")
        hots = models.WeiboHotsItem.objects.filter(time__contains = date)
        res = {}
        res["xAxisList"] = []
        res["Top1List"] = []
        res["Top2List"] = []
        res["Top3List"] = []
        res["Descs"] = []
        top1 = []
        top2 = []
        top3 = []

        for hot in hots:
            res["xAxisList"].append(hot.time[-5:])
            res["Top1List"].append(int(hot.hots[0]["count"]))
            top1.append(hot.hots[0]["content"])
            res["Top2List"].append(int(hot.hots[1]["count"]))
            top2.append(hot.hots[1]["content"])
            res["Top3List"].append(int(hot.hots[2]["count"]))
            top3.append(hot.hots[2]["content"])
        res["Descs"].append(top1)
        res["Descs"].append(top2)
        res["Descs"].append(top3)

        return http.JsonResponse(res,safe = False, status = 200)




    
class SearchView(View):
    def get(self, request):
        search_type = request.GET.get("search_type")
        
        res = models.SearchItem.objects.filter(type=search_type).order_by("-patch")

        search = serializers.serialize("json",res,ensure_ascii = False) #最强改bug
        search = json.loads(search)
        
        return http.JsonResponse(search ,safe = False, status = 200)

class AddSearchView(View):
    def get(self, request):
        content = request.GET.get("content")
        search_type = request.GET.get("type")
        mes = {}
        res = models.SearchItem.objects.filter(search_content = content,type = search_type)
        if res:
            mes["signal"] = 0
        else:
            models.SearchItem.objects.create(search_content = content,patch = 0,type = search_type)
            mes["signal"] = 1

        return http.JsonResponse(mes ,safe = False, status = 200)

class DetailView(View):
    def get(self, request):
        # json_data = json.loads(self.request.body.decode("utf-8"))
        # hot_type = json_data["hot_type"]
        content = request.GET.get("content")
        patch = request.GET.get("patch")
        detail_type = request.GET.get("detail_type")
        max_patch = models.SearchItem.objects.get(search_content = content,type = detail_type).patch
        if detail_type == "weibo":
            res = models.WeiboAnalysesItem.objects.get(search_content = content,search_patch = patch)
        elif detail_type == "zhihu":
            pass
        res_dict = model_to_dict(res)
        del(res_dict["_id"])
        res_dict["max_patch"] = max_patch
        # print(res_dict)
        # analyse = json.dumps(res_dict,ensure_ascii = False)
        # print(analyse)

        # print(analyse)
    
        # analyse = serializers.serialize("json",res,ensure_ascii = False) #最强改bug 序列化为str类型
        # analyse = json.loads(analyse) 
        # weibos = analyse[0].get("fields")["weibos"]
        # weibos = json.loads(weibos)
        # for weibo in weibos:
        #     res_count = json.loads(weibo["res_count"])
        #     weibo["res_count"] = res_count
        #     res_spirit = json.loads(weibo["res_spirit"])
        #     weibo["res_spirit"] = res_spirit
        # analyse[0]["fields"]["weibos"] = weibos
        # print(analyse[0])
        
        return http.JsonResponse(res_dict ,safe = False, status = 200)

class DetailChangeView(View):
    def get(self, request):
        content = request.GET.get("content")
        mid = request.GET.get("mid")
        time = request.GET.get("time")[0:9]

        patchs = models.WeiboAnalysesItem.objects.filter(search_content = content,parse_time__contains = time).order_by("parse_time")
        res = {}
        res["xAxisData"] = []
        res["posData"] = []
        res["negData"] = []
        for patch in patchs:
            for weibo in patch.weibos:
                if weibo["mid"] == mid:
                    res["xAxisData"].append(patch.parse_time[-8:-3])
                    res["posData"].append(weibo["res_spirit"]["positive"])
                    res["negData"].append(weibo["res_spirit"]["negative"])
                    break
        print(res)
        return http.JsonResponse(res,safe = False, status = 200)

            

