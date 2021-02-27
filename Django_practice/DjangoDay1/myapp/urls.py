from django.conf.urls import url
from django.urls import path, re_path

from myapp.views import *

urlpatterns = [
    path('hello/',hello_view),
    path('greet/<name>/',greet_view),
    path('wel/',welcome_view,{"name":"Jonda","color":"black"}),
    path('convert1/<str:name>/<int:age>/<uuid:uid>/',convert_view1),
    path('convert2/<path:info>/<slug:comment>/',convert_view2),
    re_path(r'^hi/(?P<name>\w+)/$',hi_view,{"country":"China"}),
    url(r'^test/(?P<tel>\w+)/$',url_test_view,{"home":"ShanXi"}),
]