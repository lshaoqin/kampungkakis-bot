from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.sqlite3'
db = SQLAlchemy(app)

def save_msg(name, hp_no, whatsapp_id, body):
   msg = Message(name = name, hp_no = hp_no, whatsapp_id = whatsapp_id, body = body)
   db.session.add(msg)
   db.session.commit()

def save_user(hp_no, state):
   newUser = User(hp_no = hp_no, state = state)
   db.session.add(newUser)
   db.session.commit()

def check_user(hp_no):
   #Check user by phone number
   user = User.query.filter_by(hp_no = hp_no).first()
   if user:
      #if user exists, return their state
      return user.state
   else:
      #if user does not exist, save the user and return state as default
      save_user(hp_no, 'default')
      return 'default'

#Edit user state, returns True if successful and False otherwise
def edit_user(hp_no, new_state):
   user = User.query.filter_by(hp_no=hp_no).first()
   if user:
      user.state = new_state
      db.session.commit()
      return True
   return False

class Message(db.Model):
   id = db.Column('message_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   hp_no = db.Column(db.String(12))  
   whatsapp_id = db.Column(db.String(30))
   body = db.Column(db.String(5000))

class User(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   hp_no = db.Column(db.String(12)) 
   state = db.column(db.String(50))


with app.app_context():
    db.create_all()