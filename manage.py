__author__ = 'gareth'

from Bookmarks import app,db
from flask.ext.script import Manager, prompt_bool
from Bookmarks.model import User

manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    db.session.add(User(username="falken",email="test@test.com"))
    db.session.add(User(username="John",email="john@test.com"))
    db.session.commit()
    print("Initialized the database")
@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all your data"):
        db.drop_all()
        print("Dropped the database")
if __name__ == '__main__':
    manager.run()