from django.urls import path
from reverse_app.views import *

app_name = "reverse_app"

urlpatterns = [
    path('goa/<fruit>/<color>/',go_a),
    path('handle/<f>/<c>/',handle_a,name="hd")
]