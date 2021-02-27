import sys
#sys.path.append("E:\\python1904\\FlaskDay3")  这一招也可以
sys.path.append(".")   # 将命令行中的当前目录作为搜索路径之一

from flask_script import Manager

from HomeworkApp.views import app

manager = Manager(app)


if __name__ == '__main__':
    manager.run()