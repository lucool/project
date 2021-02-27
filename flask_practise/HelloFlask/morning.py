from flask import Flask

app = Flask(__name__)


@app.route("/hello/")
def hello_view():
    return "<h3 style='color:blue'>Hello,Flask!</h3>"


@app.route("/hi/<name>/")
def hi_view(name):
    return "hi " + name


@app.route("/stu/<int:age>/<float:score>/")
def stu_view(age,score):
    age += 2
    score += 5
    return "age+=2结果为：" + str(age) +";score+=5结果是：" + str(score)


@app.route("/greet/<path:info>/")
def greet_view(info):
    return "接收到的info是：" + info


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)