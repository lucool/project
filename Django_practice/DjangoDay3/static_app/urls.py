from django.urls import path

from static_app.views import show_view

urlpatterns = [
    path('show/',show_view),
]