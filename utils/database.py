from datetime import date
import sqlite3

__connection = None

def create_connection(path: str):
  global __connection
  __connection = sqlite3.connect(path)
  return __connection


def setup():
  cur = __connection.cursor()
  cur.execute("""CREATE TABLE IF NOT EXISTS members ( 
              first_name TEXT, 
              last_name TEXT, 
              address TEXT, 
              city TEXT, 
              email_address TEXT, 
              mobile_phone TEXT, 
              registration_date DATE, 
              membership_id INTEGER 
  );""")
  cur.execute("""CREATE TABLE IF NOT EXISTS users ( 
              first_name TEXT, 
              last_name TEXT, 
              username TEXT, 
              password TEXT, 
              authorization_level INTEGER, 
              registration_date DATE 
  );""")
  cur.execute(f"""INSERT INTO users 
              SELECT 'Jamey', 'Schaap', 'admin', '123', 2, '{date.today()}'
              WHERE NOT EXISTS (SELECT * FROM users)
              ;""")
  __connection.commit()

  
def execute_query(query: str, *args: any):
  query = query.strip()
  
  expected_amount_args = query.count("?")
  if (expected_amount_args != len(args)):
    raise 
  
  for arg in args:
    query = query.replace("?", str(arg).replace("\'", "\'\'"), 1)
    
  cur = __connection.cursor()
  
  cur.execute(query)
  
  if query[0:6].upper() == "SELECT":
    return cur.fetchall()
  else:
    __connection.commit()
  
  