from django.urls import path

from homework_app.views import *

app_name = "homework_app"

urlpatterns = [
    path('login/',login_view,name="log"),
    path('success/',success_view,name='suc')
]