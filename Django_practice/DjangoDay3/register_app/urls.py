from django.urls import path

from register_app.views import *

app_name = "register_app"

urlpatterns = [
    path('register/',register_view,name="register"),
    path('success/<username>/',success_view,name="suc")
]