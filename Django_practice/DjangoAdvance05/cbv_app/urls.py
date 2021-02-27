from django.urls import path

from cbv_app.views import *

app_name = "cbv_app"

urlpatterns = [
    path('login/',LoginView.as_view()),
    path('success/',SuccessView.as_view(),name="suc")
]