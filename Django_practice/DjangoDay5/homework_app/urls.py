from django.urls import path

from homework_app.views import *

app_name = "homework_app"

urlpatterns = [
    path("addschool/",add_school_view,name="school"),
    path('addstudent/',add_student_view,name="student"),
    path('students/',show_students,name="students"),
    path('school',detail_school_view,name="detail_school")
]