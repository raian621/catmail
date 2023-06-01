from flask import Flask, Response, request, render_template
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
from os import path, environ
import json

import load_config

app = Flask(__name__)
db = None

def connect_to_db(db_URI):
  app.config['SQLALCHEMY_DATABASE_URI'] = db_URI
  db = SQLAlchemy(app)

@app.route('/', methods=['GET'])
def home():
  return Response('Hello GET')

@app.post('/')
def post():
  return Response('Hello POST')

@app.post('/send-to')
def send_to():
  print(request.args)
  if ('recipient', 'email-template') not in request.args:
    return Response(status=400)
  recipient_address = request.args['recipient']
  email_template = request.args['email-template']
  
  data = request.data
  body = None
  if data:
    body = json.loads(data)

  return Response(json.dumps(
    {
      'recipient': recipient_address,
      'email-template': email_template,
      'body': body
    }
  ), content_type='application/json')

@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
  # return Response('Hello', status=200)
  return render_template('admin/login.html')
