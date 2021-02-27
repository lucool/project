import sys
sys.path.append(".")   # 将命令行中的当前目录追加到Python搜索路径中

from flask_script import Manager

from BlueApp import create_app

app = create_app()
manager = Manager(app)


if __name__ == '__main__':
    manager.run()