from django.urls import path
from ajax_app.views import ajax_upload_view

app_name = "ajax_app"

urlpatterns = [
    path('upload/',ajax_upload_view,name="up"),
]