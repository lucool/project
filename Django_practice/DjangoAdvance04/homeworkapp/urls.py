from django.urls import path

from homeworkapp.views import *

urlpatterns = [
    path('fruits/',fruits_view),
    path('students/',students_view)
]