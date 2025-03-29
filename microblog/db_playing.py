from app import db
from app import app
from app.models import User, Post


with app.app_context():
    u = User(username='john', email='john@example.com')
    db.session.add(u)
    db.session.commit()
    users = User.query.all()
    print(users)

    #db.create_all()
    #admin_role = Role(name = 'Admin')
    #db.session.add(admin_role)
    #db.session.commit()
    #user_john = User(username = 'John', role = admin_role)
    #db.session.add(user_john)
    #db.session.commit()

