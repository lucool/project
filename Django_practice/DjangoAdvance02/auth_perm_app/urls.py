from django.urls import path

from auth_perm_app.views import *

app_name = "auth_perm_app"

urlpatterns = [
    path('register/',register_view,name="reg"),
    path('login/',login_view,name="log"),
    path('welcome/',welcome_view,name='wel'),
    path('logout/',logout_view,name="out")
]