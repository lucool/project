import sys
sys.path.append(".")

from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
print("1111111")
from HomeworkApp import create_app
from HomeworkApp.models import db

app = create_app()
Migrate(app,db)
manager = Manager(app)
manager.add_command("nicedb",MigrateCommand)   # 自定义迁移命令

if __name__ == '__main__':
    manager.run()