from django.urls import path

from homework_app.views import *

app_name = "homework_app"

urlpatterns = [
    path('goa/',go_a),
    path('handlea/<hobby>/',handle_a,name="handle"),
    path('fruits/',fruit_view),
    path('custom/',custom_view),
    path('<info>/',sports_view),
]