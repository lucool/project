from django.urls import path

from formapp.views import *

app_name = "formapp"

urlpatterns = [
    path('register/',register_view,name="reg"),
    path('success/',success_view,name="suc")
]