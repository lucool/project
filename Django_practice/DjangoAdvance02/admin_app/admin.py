from django.contrib import admin

from admin_app.models import Fruit

admin.site.register([Fruit,])  # 注册模型，方便后台管理
