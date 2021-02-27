from django.core.paginator import Paginator
from django.shortcuts import render

from page_app.models import Student


def students_view(request,pagenumber=1):
    students = Student.objects.all()
    paginator = Paginator(students,3)   #  每页最多显示3条记录
    if pagenumber > paginator.num_pages:
        pagenumber -= 1
    if pagenumber < 1:
        pagenumber += 1
    page = paginator.page(pagenumber)   #  根据页码参数，获取对应的记录，封装到Page对象中
    return render(request,'page_app/students.html',locals())