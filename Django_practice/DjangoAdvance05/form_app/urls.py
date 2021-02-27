from django.urls import path

from form_app.views import *

app_name = "form_app"

urlpatterns = [
    path('register/',register_view,name="reg"),
    path('success/',success_view,name="suc")
]