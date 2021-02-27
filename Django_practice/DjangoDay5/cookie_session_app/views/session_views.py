from django.http import HttpResponse


def add_session_view(request):
    request.session["username"] = "tom"
    request.session["password"] = "123456"
    print("sessionid为：",request.session.session_key)
    return HttpResponse("session属性添加完毕~~~")


def get_session_data(request,name):
    value = request.session.get(name,"没有该名称的session属性")
    return HttpResponse(value)


def del_session_data(request,name):
    try:
        del request.session[name]
    except:
        return HttpResponse("没有该名称的session属性，删除失败！")
    return HttpResponse("Session中的该属性已经成功删除！")


def flush_session(request):
    request.session.flush()
    return HttpResponse("session已清空！")

