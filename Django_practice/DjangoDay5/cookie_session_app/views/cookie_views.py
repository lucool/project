from django.http import HttpResponse


def add_cookie_view(request):
    response = HttpResponse("<h4>Cookie成功添加~~~</h4>")
    response.set_cookie("sport","football")   # 默认存储于浏览器缓存中，浏览器重启后该Cookie消失
    response.set_cookie("fruit","apple",max_age=60)  # 设置Cookie的保存时间为60秒
    return response


def show_cookies_view(request):
    html = ""
    for k,v in request.COOKIES.items():
        html += k
        html += "===========>"
        html += v
        html += "<br/>"
    return HttpResponse(html)


def get_cookie_view(request,name):
    cookie_value = request.COOKIES.get(name,"没有该Cookie!")
    result = "cookie名称为" + name + "对应的值为：" + cookie_value
    return HttpResponse(result)


def delete_cookie_view(request,name):
    response = HttpResponse("<h4>名称为"+name+"的Cookie已经删除！</h4>")
    response.delete_cookie(name)
    return response