import sys
sys.path.append(".")

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from RelationApp import create_app
from RelationApp.models.one_one import db
from RelationApp.models.many_many import db

app = create_app()
Migrate(app,db)
manager = Manager(app)
manager.add_command("nicedb",MigrateCommand)   # 自定义迁移命令

if __name__ == '__main__':
    manager.run()