from flask import Flask, Response

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
  return Response('Hello GET')

@app.post('/')
def post():
  return Response('Hello POST')