from flask import Flask

app = Flask(__name__)   # 实例化Flask程序实例


@app.route("/hello/")   #  使用程序实例的route()方法作为装饰器
def hello_view():
    return "<h3 style='color:red'>Hello,Flask~~~</h3>"


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8888,debug=True)    #  启动Flask服务