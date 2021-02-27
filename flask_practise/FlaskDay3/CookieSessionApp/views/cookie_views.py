from flask import Blueprint, make_response, request

blue1 = Blueprint("cookie_blue",__name__)


@blue1.route("/nice/")
def nice_view():
    return "<h3 style='color:blue'>You are so nice~~~</h3>"


@blue1.route("/addcookie/")
def add_cookie():
    response = make_response("<h3>Cookie创建成功！</h3>")
    response.set_cookie("sport","football",max_age=60)  # 设置Cookie，保存时间为60秒
    response.set_cookie("food","noodles")  # max_age为None时，代表该Cookie存在于浏览器缓存中，浏览器重启后，该Cookie消失
    response.set_cookie("country","Japan")
    return response


@blue1.route("/delcookie/<name>/")
def delete_cookie(name):
    response = make_response("<h3 style='color:red'>名称为"+name+"的Cookie已经删除！</h3>")
    response.delete_cookie(name)   # 删除指定名称的Cookie
    return response


@blue1.route("/cookie/<name>/")
def get_cookie(name):
    value = request.cookies.get(name,"没有该Cookie")
    return "名称为" + name + "的Cookie对应的value是：" + value


@blue1.route("/cookies/")
def get_cookies():
    cookies = request.cookies
    html = ""
    for k,v in cookies.items():    # 遍历所有Cookie
        html += k
        html += "========>"
        html += v
        html += "<br/>"
    return html