from flask import Blueprint, session

blue2 = Blueprint("session_blue",__name__)


@blue2.route("/addsession/")
def add_session():
    session["username"] = "tom"    # 设置session会话的属性（属性名、属性值）
    session["password"] = "123456"
    return "session设置成功！"


@blue2.route("/sessions/")
def get_sessions():
    html = ""
    for k,v in session.items():   # 遍历session
        html += k
        html += "==========>"
        html += v
        html += "<br/>"
    return html


@blue2.route("/pop/<name>/")
def pop_session(name):
    session.pop(name,"当前session没有该属性")
    return "session名称为" + name + "的属性已经删除!"


@blue2.route("/session/<name>/")
def get_session(name):
    value = session.get(name,"当前session没有该属性")
    return "session名称为" + name + "的属性对应的值是：" + value


@blue2.route("/clear/")
def clear_session():
    session.clear()
    return "session已清空！"
