from django.urls import path

from homework_app.views import *

app_name = "homework_app"

urlpatterns = [
    path('go/',go_fruits),
    path('send/',send_fruits,name="fruits")
]