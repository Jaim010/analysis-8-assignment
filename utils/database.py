from datetime import datetime
import sqlite3
from utils.encryption import encrypt

__connection = None

def create_connection(path: str) -> sqlite3.Connection:
  global __connection
  __connection = sqlite3.connect(path)
  return __connection


def setup() -> None:
  assert __connection != None
  cur = __connection.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS members ( 
              first_name TEXT, 
              last_name TEXT, 
              address TEXT, 
              city TEXT, 
              email_address TEXT, 
              mobile_phone TEXT, 
              registration_date TEXT, 
              membership_id INTEGER 
  );""")
  cur.execute("""CREATE TABLE IF NOT EXISTS users ( 
              first_name TEXT, 
              last_name TEXT, 
              username TEXT, 
              password TEXT, 
              authorization_level INTEGER, 
              registration_date TEXT,
              forced_password_udpate INTEGER DEFAULT 1
  );""")
  cur.execute(f"""INSERT INTO users 
              SELECT '', '', '{encrypt("superadmin")}', '{encrypt("Admin321!")}', 3, '{str(datetime.now())}', 1
              WHERE NOT EXISTS (SELECT * FROM users)
              ;""")
  __connection.commit()

  
def execute_query(query: str, *args: any) -> None or list:
  query = query.strip()
  
  expected_amount_args = query.count("?")
  if (expected_amount_args != len(args)):
    raise 
  
  assert __connection != None
  
  for arg in args:
    if type(arg) == str:
      fomatted_arg = "\'" + arg.replace("\'", "\'\'") + "\'"
      query = query.replace("?", fomatted_arg, 1)
    else:
      query = query.replace("?", str(arg), 1)
    
  cur = __connection.cursor()
  
  cur.execute(query)
  
  if query[0:6].upper() == "SELECT":
    result = cur.fetchall()
    for row in result:
      for field in row:
        if type(field) == str:
          field = field.replace("\'\'", "\'")
    return result
  
  else:
    __connection.commit()
