from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests
from twilio.twiml.messaging_response import MessagingResponse
from interactions import default_interactions

app = Flask(__name__)
app.debug=True
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.sqlite3'

db = SQLAlchemy(app)

class Message(db.Model):
   id = db.Column('message_id', db.Integer, primary_key = True)
   name = db.Column(db.String(100))
   hp_no = db.Column(db.String(12))  
   whatsapp_id = db.Column(db.String(30))
   body = db.Column(db.String(5000))

class User(db.Model):
   id = db.Column('user_id', db.Integer, primary_key = True)
   hp_no = db.Column(db.String(12)) 
   state = db.Column(db.String(50))

def init_db(app):
    db.init_app(app)

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


@app.route('/bot', methods=['POST'])
def bot():


    # save message to database
    name = request.values.get('ProfileName', '')
    whatsapp_id = request.values.get('AccountSid', '')
    hp_no = request.values.get('WaId', '')
    body = request.values.get('Body', '')
    msg = save_msg(name, hp_no, whatsapp_id, body)

    #create response instance
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    
    user_state = check_user(hp_no)

    if user_state == 'default': 
        # Check whether the message matches a template
        action = default_interactions.get(body)
        # If message matches a template, change to corresponding state and set response
        if (action):
            edit_user(hp_no, action['state'])
            msg.body(action['reply'])
            responded = True

    #if user's message doesn't match any of the recognised responses
    if not responded:
        msg.body('Thank you for contacting KampungKakis! Please identity who you are so we can help you better: ')
    return str(resp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(port=4000)