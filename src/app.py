from flask import Flask, Response, request
from dotenv import load_dotenv
from os import path, environ
import json

APP_SHOULD_EXIT = False

dotenv_path = path.join(path.dirname(__file__), '.env')
load_dotenv(dotenv_path)
def check_environment_variables():
  required_env_vars = [
    'EMAIL_ADDRESS',
    'EMAIL_PASSWORD',
    'SMTP_PORT',
    'SMTP_HOST',
    'DB_USERNAME',
    'DB_PASSWORD',
    'DB_HOSTNAME',
    'DB_PORT'
  ]
  for var in required_env_vars:
    if var not in environ.keys():
      global APP_SHOULD_EXIT
      APP_SHOULD_EXIT = True
      print(f'[CONFIG ERROR] Required environment variable \'{var}\' not defined.')
check_environment_variables()

if APP_SHOULD_EXIT:
  print('ERROR(S) occurred, exiting program...')
  exit(1)

app = Flask(__name__)


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
