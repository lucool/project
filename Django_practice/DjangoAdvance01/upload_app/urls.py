from django.urls import path

from upload_app.views import *

app_name = "upload_app"

urlpatterns = [
    path('form/',form_upload,name="form"),
    path('success/<path>/',success_view,name='suc')
]