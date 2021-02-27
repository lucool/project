from django.urls import path

from jsonapp.views import *

urlpatterns = [
    path('jsonobj/',json_object_view),
    path('jsonarray/',json_array_view)
]