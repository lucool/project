import sys
sys.path.append(".")

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from RestfulApp import create_app
from RestfulApp.models import db

app = create_app()
Migrate(app,db)
manager = Manager(app)
manager.add_command("nicedb",MigrateCommand)

if __name__ == '__main__':
    manager.run()