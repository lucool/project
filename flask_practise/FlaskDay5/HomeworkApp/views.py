from flask import Blueprint, request, render_template, redirect, url_for
print("555555555")
from HomeworkApp.ext import db
from HomeworkApp.models import School, Student

blue = Blueprint("myblue",__name__)


@blue.route("/school/",methods=["GET","POST"])
def school_view():
    if request.method == "GET":
        return render_template("add_school.html")
    elif request.method == "POST":
        school_name = request.form.get("school_name")
        school_address = request.form.get("school_address")
        new_school = School(name=school_name,address=school_address)
        db.session.add(new_school)
        db.session.commit()
        return redirect(url_for("myblue.school_view"))   # 重定向到添加学校页面


@blue.route("/student/",methods=["GET","POST"])
def student_view():
    if request.method == "GET":
        schools = School.query.all()   # 进入添加学生页面前，先查询所有的学校
        return render_template("add_student.html",all_schools=schools)
    elif request.method == "POST":
        student_name = request.form.get("student_name")
        student_score = request.form.get("student_score")
        student_school_id = request.form.get("student_school")   # 获取学生所在学校的ID
        new_student = Student(name=student_name,score=student_score,school_id=student_school_id)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for("myblue.student_view"))  # 重定向到添加学生页面
