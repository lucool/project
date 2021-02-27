from flask import Flask, make_response, redirect

app = Flask(__name__)   # 实例化Flask程序实例


@app.route("/student/<string:name>/<int:score>/")
def student_view(name,score):
    response = make_response("我叫"+name+"；考了"+str(score)+"分")
    return response


@app.route("/vip/<name>/<path:info>/<home>/")
def vip_view(home,info,name):
    return "经过path转换器得到的info：" + info


@app.route("/test/<nickname>/")
def test_view(nickname):
    return redirect("http://httpbin.org/get?haha="+nickname)