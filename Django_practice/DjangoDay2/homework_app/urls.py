from django.urls import path

from homework_app.views import *

urlpatterns = [
    path('hello/',hello_view),
    path('register/<regname>/<regpwd>/',register_view),
    path('<info>/',planet_view),
]