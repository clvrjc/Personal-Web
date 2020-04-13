#Libraries to be import START
import random
from flask import Flask, request, g, session, render_template, redirect, url_for, flash
import os
import json
import time, string, random, re
import pymongo
from pymongo import MongoClient

from flask import Flask
from flask_mail import Mail, Message

list_of_qoutes = ["“If you make customers unhappy in the physical world, they might tell 6 friends. If you make customers happy on the Internet, they can each tell 6,000 friends.” – Jeff Bezos","“There’s a way to do it better – find it.” –Thomas A. Edison","“If you make customers unhappy in the physical world, they might tell 6 friends. If you make customers happy on the Internet, they can each tell 6,000 friends.” – Jeff Bezos","“For the things we have to learn before we can do them, we learn by doing them.” ― Aristotle"]

app = Flask(__name__)
'''
need to auth with gmail
mail= Mail(app)
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'jearbecerro@gmail.com'#os.env
app.config['MAIL_PASSWORD'] = 'wal*********'#os.env
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)

@app.route("/send")
def send_email():
	msg = Message('Subject - Hellow', sender = 'rolandobecerro@gmail.com', recipients = ['jearbecerro@gmail.com'])
	msg.body = "Hello Flask message sent from Flask-Mail"
	mail.send(msg)
	return "Sent"
'''
@app.route("/send", methods=['GET','POST'])
def send_email():
	return "success"

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')


if __name__ == "__main__":
	app.run(debug=True,port='4040')
 
