from typing import Tuple
import utils.database as database
from utils.user import User

def login(app, username: str, password: str ) -> bool:
  (is_valid, user) = __validate_login(username, password)
  if (is_valid):
    app.user = User(user[0], user[1], user[2], user[4], user[5])
    return True
  return False

def __validate_login(username: str, password: str):
  users = database.execute_query("SELECT * FROM users WHERE username='?' AND password='?'", username, password)
  
  if len(users) == 0:
    return (False, ())
  if len(users) > 1:
    raise ("")
  
  user = users[0]
  return (True, user)

def logout(app):
  app.user = None