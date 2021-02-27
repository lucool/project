import sys
sys.path.append(".")

from flask_migrate import Migrate, MigrateCommand
from RelationApp import create_app
from flask_script import Manager
from RelationApp.models import db


app = create_app()
Migrate(app,db)    #  目的是可以创建migrations目录
manager = Manager(app)
manager.add_command("nicedb",MigrateCommand)   #  自定义一个迁移命令，自定义命令名称为"nicedb"

if __name__ == '__main__':
    manager.run()