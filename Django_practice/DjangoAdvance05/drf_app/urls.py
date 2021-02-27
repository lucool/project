from django.urls import path

from drf_app.views import fruit_view

urlpatterns = [
    path('fruit/<int:fruit_id>/',fruit_view)
]