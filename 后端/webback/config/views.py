from django.views import View
import json
from config import models
from django import http
from django.core import serializers
# Create your views here.


class ConfigView(View):
    def get(self, request):
        # cookie_type = json_data['cookie_type'] #需要传送cookie类型
        try:        
             # 读取configs信息
            configs = serializers.serialize("json",models.ConfigMes.objects.all())
            configs = json.loads(configs)
            return http.JsonResponse({"configs":configs},status = 200)
        except models.ConfigMes.DoesNotExist:
            return http.HttpResponse("未查找到任何配置信息",status = 404)
    def post(self, request):

        json_data = json.loads(self.request.body.decode("utf-8"))
        parse_type = json_data["parse_type"]
        headers = json_data["headers"]
        cookies = json_data["cookies"]
        status = json_data["status"]
    

        try:        
            config = models.ConfigMes.objects.filter(parse_type = parse_type)
            config.update(headers = headers,cookies = cookies,status = status)
            return http.JsonResponse({"message":"更新成功，待验证中"},status = 200)
        except e:
            return http.HttpResponse("更新失败",status = 404)

    