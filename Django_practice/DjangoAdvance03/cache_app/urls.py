from django.urls import path

from cache_app.views import *

urlpatterns = [
    path('cache/',fruits_view),
    path('redis/',fruits_redis_view),
    path('page/',page_view)
]