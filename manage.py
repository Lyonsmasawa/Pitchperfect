from imghdr import tests
from re import S
from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand

#calls the create app function with the config so as to create the app instance
app = create_app('development')

#instantiate manager class
manager = Manager(app)
#this command launches our server
manager.add_command('server', Server) 

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)

@manager.command #create new command
def test():
    import unittest
    tests = unittest.TestLoader.discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

if __name__ == '__main__':
    manager.run()

