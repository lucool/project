from django.urls import path

from homework_app.views import *

app_name = "homework_app"

urlpatterns = [
    path('login/',login_view,name="login"),
    path('success/',success_view,name='suc'),
    path('tokenlogin/',login_token_view),
    path('tokensuccess/',success_token_view)
]