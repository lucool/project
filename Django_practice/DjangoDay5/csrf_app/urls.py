from django.urls import path

from csrf_app.views import *

app_name = "csrf_app"

urlpatterns = [
    path('register/',register_view,name="reg"),
    path('success/<regname>/',success_view,name='suc'),
    path('login/',login_view,name='log'),
    path('welcome/<logname>/',welcome_view,name='wel')
]