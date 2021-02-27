from flask import Flask
from flask_script import Manager

app = Flask(__name__)
m = Manager(app)   #  创建Manager对象，通过构造方法与Flask程序实例关联


@app.route("/nice/")
def nice_view():
    return "<h3 style='color:green'>You are so nice~~~</h3>"


@m.command   # Manager对象注册了一个命令
def my_command(address,email):
    return "我的地址是：" + address +"；我的邮箱是：" + email


if __name__ == '__main__':
    m.run()    #  使用Manager对象启动Flask应用