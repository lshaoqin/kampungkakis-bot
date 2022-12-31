from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests
from twilio.twiml.messaging_response import MessagingResponse
from db import save_msg, edit_user, check_user, init_db
from interactions import default_interactions

app = Flask(__name__)
app.debug=True
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.sqlite3'

init_db(app)

@app.route('/bot', methods=['POST'])
def bot():

    # save message to database
    name = request.values.get('ProfileName', '')
    whatsapp_id = request.values.get('AccountSid', '')
    hp_no = request.values.get('WaId', '')
    body = request.values.get('Body', '').lower()
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
        app.run(port=4000)