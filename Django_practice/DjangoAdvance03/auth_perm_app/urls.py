from django.urls import path

from auth_perm_app.views import *

app_name = "auth_perm_app"

urlpatterns = [
    path('login/',login_view,name='log'),
    path('students/',students_view,name='students'),
    path("up/",update_view)
]