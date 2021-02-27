from django.shortcuts import render, redirect
from django.urls import reverse

from homework_app.models import School, Student


def add_school_view(request):    #  添加学校视图
    if request.method == "GET":
        return render(request,'homework_app/add_school.html')
    elif request.method == "POST":
        schoolname = request.POST.get("schoolname")
        schooladdress = request.POST.get("schooladdress")
        School.objects.create(name=schoolname,address=schooladdress)
        return redirect(reverse("home:school"))


def add_student_view(request):    # 添加学生视图
    if request.method == "GET":
        schools = School.objects.all()   # 查询所有学校
        return render(request,'homework_app/add_student.html',{"schools":schools})
    elif request.method == "POST":
        studentname = request.POST.get("studentname")
        studentsex = request.POST.get("studentsex")
        studentscore = request.POST.get("studentscore")
        school_id = request.POST.get("school_id")
        Student.objects.create(name=studentname,sex=studentsex,score=studentscore,school_id=school_id)
        return redirect(reverse("home:students"))


def show_students(request):
    students = Student.objects.all()
    return render(request,'homework_app/students.html',locals())


def detail_school_view(request):
    schoolid = request.GET.get("schoolid")   # 接收学校ID
    school = School.objects.get(pk=schoolid)
    return render(request,'homework_app/school_detail.html',{"school":school})







