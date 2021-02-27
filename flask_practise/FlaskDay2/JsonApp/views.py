from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/student/")
def student_view():
    student_dict = {"name":"tom","age":25,"score":83.5}
    return jsonify(student_dict)   # 向客户端发送对象格式的JSON


@app.route("/students/")
def students_view():
    stu1 = {"name":"tom","age":25,"score":83.5}
    stu2 = {"name":"jerry","age":26,"score":87}
    stu3 = {"name": "alice", "age":29, "score":60}
    students = [stu1,stu2,stu3]
    return jsonify(students)   # 向客户端发送数组格式的JSON