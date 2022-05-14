from typing import Tuple
from responses.login_response import LoginResponse
from utils import Database
from utils.user import User

def login(username: str, password: str ) -> bool:
  (is_valid, user) = __validate_login(username, password)
  if (is_valid):
    User().first_name = user[0]
    User().last_name = user[1]
    User().username = user[2]
    User().authorization_level = user[4]
    User().registration_date = user[5]
    return True
  return False

def __validate_login(username: str, password: str):
  users = Database().select_user_by_username_password(username, password)
  
  print(len(users) != 0)
  if len(users) == 0:
    return (False, ())
  if len(users) > 1:
    raise ("")
  
  user = users[0]
  return (True, user)

def logout():
  User().username = None
  User().authorization_level = None