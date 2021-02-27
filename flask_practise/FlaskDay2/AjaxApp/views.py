import pymysql
from flask import Flask, render_template, jsonify, url_for


def get_conn():    #  获取数据库连接
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="mydb",
        charset='utf8'
    )
    return conn

def check_db(username):   # 查询数据库中是否存在该用户名
    conn = get_conn()
    cursor = conn.cursor()
    sql = "select * from users where username='{}'".format(username)
    try:
        cursor.execute(sql)   # 执行查询
        item = cursor.fetchone()
        conn.commit()
        if item:
            return True    #  说明数据库中已经存在该用户名
        else:
            return False    #  数据库中不存在该用户名
    except Exception as e:
        print("发生异常啦，异常是：",e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()


app = Flask(__name__)   #  创建Flask程序实例


@app.route("/register/")
def register_view():
    return render_template("register.html")  # 加载到注册页面


@app.route("/check/<username>/")
def check_view(username):
    is_exists = check_db(username)
    if is_exists:
        data = {
            "code":"555",
            "msg":"该用户名已存在，请选择其他用户名！"
        }
    else:
        data = {
            "code":"666",
            "msg":"恭喜，该用户可以注册~~~"
        }
    return jsonify(data)    # 向前端发送JSON数据


@app.route("/sex/")
def go_sex():
    return render_template("sex.html")


@app.route("/nice/<select_sex>/")
def sex_view(select_sex):
    if select_sex == "boy":
        data = {
            "pic_path":url_for("static",filename="images/boy.jpg")
        }
    else:
        data = {
            "pic_path": url_for("static", filename="images/girl.jpg")
        }
    print("后台url_for()获取的静态资源路径是："+data["pic_path"])
    return jsonify(data)


