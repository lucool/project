from flask import Flask

app = Flask(__name__)


@app.route("/hi/<name>/")
def hi_view(name):
    return "<h3>hi,<span style='color:green'>" + name + "</span></h3>"


@app.route("/student/<int:age>/<float:score>/")
def student_view(age,score):
    age += 1
    score += 5
    return "明年" + str(age) + "岁;添加5分后的得分：" + str(score)


@app.route("/greet/<path:info>/")
def greet_view(info):
    return "path转换器作用后，接收到的info是：" + info


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)