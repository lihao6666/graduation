
```
后端
└─ webback
   ├─ config              # 设置APP
   │  ├─ __init__.py
   │  ├─ admin.py      
   │  ├─ apps.py
   │  ├─ migrations
   │  │  ├─ 0001_initial.py
   │  ├─ models.py       # 模型ORM
   │  ├─ tests.py        # 测试文件
   │  ├─ urls.py         # URL配置
   │  └─ views.py        # 业务视图
   ├─ manage.py
   ├─ parse              # 爬虫APP
   │  ├─ Serialize.py
   │  ├─ __init__.py
   │  ├─ admin.py
   │  ├─ apps.py
   │  ├─ migrations
   │  ├─ models.py
   │  ├─ tests.py
   │  ├─ urls.py
   │  └─ views.py
   └─ webback
      ├─ __init__.py
      ├─ asgi.py
      ├─ settings.py    #后端配置
      ├─ urls.py        #总路由配置
      └─ wsgi.py

```