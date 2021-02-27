from django.urls import path

from page_app.views import students_view

app_name = "page_app"

urlpatterns = [
    path('students/',students_view),
    path('students/<int:pagenumber>/',students_view,name="stu"),
]