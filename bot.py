from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import requests
from twilio.twiml.messaging_response import MessagingResponse
from db import save_msg, message

app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///messages.sqlite3'

@app.route('/bot', methods=['POST'])
def bot():

    # save message to database
    name = request.values.get('ProfileName', '')
    whatsapp_id = request.values.get('AccountSid', '')
    hp_no = request.values.get('WaId', '')
    body = request.values.get('Body', '').lower()
    msg = save_msg(name, hp_no, whatsapp_id, body)
    print(msg.query.all())

    #create response instance
    resp = MessagingResponse()
    msg = resp.message()
    responded = False


    if 'quote' in body:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in body:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True

    #if user's message doesn't match any of the recognised responses
    if not responded:
        msg.body('Thank you for contacting KampungKakis! Please identity who you are so we can help you better: ')
    return str(resp)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=4000)