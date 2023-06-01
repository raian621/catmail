from secrets import token_urlsafe
from argon2 import PasswordHasher

def create_key(name, sql_db):
  apikey = token_urlsafe(32)
  
  return apikey