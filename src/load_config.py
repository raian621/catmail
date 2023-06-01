from dotenv import load_dotenv
from os import path, environ
from argon2 import PasswordHasher

APP_SHOULD_EXIT = False

dotenv_path = path.join(path.dirname(__file__), '.env')
db_env_path = path.join(path.dirname(__file__), 'db.env')
redis_env_path = path.join(path.dirname(__file__), 'redis.env')
adminpass_path = path.join(path.dirname(__file__), '.adminpass')

load_dotenv(dotenv_path)
load_dotenv(db_env_path)
load_dotenv(redis_env_path)

def check_environment_variables():
  required_env_vars = [
    'REDIS_URI',
    'REDIS_PORT',
    'DB_PROVIDER',
    'DB_URI',
    'DB_PORT',
    'ADMIN_USERNAME',
    'ADMIN_PASSWORD',
    'HOST',
    'PORT'
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

if not path.exists(adminpass_path):
  with open(adminpass_path, 'w+') as file:
    username = environ.get('ADMIN_USERNAME')
    password = environ.get('ADMIN_PASSWORD')
    hashed_password = PasswordHasher().hash(password)
    file.write(f'{username}:{hashed_password}')