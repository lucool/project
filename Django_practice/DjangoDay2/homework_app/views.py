import pymysql
from django.http import HttpResponse
from django.shortcuts import render


def hello_view(request):
    return HttpResponse("<h3 style='color:green'>Hello,Django!</h3>")

def planet_view(request,info):
    if info == "sun":
        return HttpResponse("<h3 style='color:red'>灿烂的太阳</h3>")
    elif info == "star":
        return HttpResponse("<h3 style='color:blue'>闪烁的星星</h3>")
    else:
        return HttpResponse("<h3 style='color:yellow'>漂亮的月亮~~~</h3>")


def register_view(request,regname,regpwd):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='123456',
        database='mydb',
        charset='utf8'
    )
    cursor = conn.cursor()
    sql = "insert into users(username,password)values(%s,%s)"   # 使用%s作为参数的占位符
    try:
        cursor.execute(sql,(regname,regpwd))   #  在执行SQL的时候传递参数
        conn.commit()
        return HttpResponse("<h3 style='color:green'>恭喜，注册成功！</h3>")
    except Exception as e:
        print("注册异常，异常原因：",e)
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
