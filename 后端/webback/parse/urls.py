from django.urls import path

from . import views

app_name = "parse"

urlpatterns = [
    path('hots', views.HotView.as_view(), name='hots'),
    path('hotschange', views.HotChangeView.as_view(), name='hotschange'),
    path('search', views.SearchView.as_view(), name='search'),
    path('addsearch', views.AddSearchView.as_view(), name='addsearch'),
    path('detail', views.DetailView.as_view(), name='detail'), #分析结果
    path('detailchange', views.DetailChangeView.as_view(), name='detailchange'), #分析结果变化

]