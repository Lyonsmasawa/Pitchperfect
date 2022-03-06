from re import S
from app import create_app
from flask_script import Manager, Server

#calls the create app function with the config so as to create the app instance
app = create_app('development')

#instantiate manager class
manager = Manager(app)
#this command launches our server
manager.add_command('server', Server) 

if __name__ == '__main__':
    manager.run()

