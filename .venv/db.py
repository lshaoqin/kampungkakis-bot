from flask_sqlalchemy import SQLAlchemy
from flask import Flask

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.sqlite3'

db = SQLAlchemy(app)
class message(db.Model):
   id = db.Column('message_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   hp_no = db.Column(db.String(12))  
   whatsapp_id = db.Column(db.String(30))
   body = db.Column(db.String(5000))


def __init__(self, name, hp_no, whatsapp_id, body):
   self.name = name
   self.hp_no = hp_no
   self.whatsapp_id = whatsapp_id
   self.body = body

def save_msg(name, hp_no, whatsapp_id, body):
   msg = message(name = name, hp_no = hp_no, whatsapp_id = whatsapp_id, body = body)
   db.session.add(msg)
   db.session.commit()

with app.app_context():
    db.create_all()