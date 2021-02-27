from django.urls import path

from middle_app.views import *

urlpatterns = [
    path('hello/<name>/',hello_view),
    path('visit/',visit_view)
]