from datetime import date
import sqlite3
from sqlite3 import Error
import os.path

from utils.singleton import Singleton

class Database(metaclass=Singleton):
  def __init__(self) -> None:
    self.__connection = None

  def create_connection(self, db_file: str) -> sqlite3.Connection:
    if self.__connection != None:
      return self.__connection
    
    create_tables = False
    if not os.path.exists(db_file):
      create_tables = True
      
    try:
      self.__connection = sqlite3.connect(db_file)
      
      if (create_tables):
        cur = self.__connection.cursor()
        cur.execute("CREATE TABLE members ( first_name TEXT, last_name TEXT, address TEXT, city TEXT, email_address TEXT, mobile_phone TEXT, registration_date DATE, membership_id INTEGER );")
        cur.execute("CREATE TABLE users ( first_name TEXT, last_name TEXT, username TEXT, password TEXT, authorization_level INTEGER, registration_date DATE );")
        cur.execute(f"INSERT INTO users ( first_name, last_name, username, password, authorization_level, registration_date) VALUES ('Jamey', 'Schaap', 'admin', '123', 2, '{date.today()}')")
        self.__connection.commit()
        
    except Error as e:
      print(e)
      
    return self.__connection
    
  def select_user_by_username_password(self, username: str, password: str) -> list:
    cur = self.__connection.cursor()
    
    query = """
            SELECT * 
            FROM users 
            WHERE username='{0}' AND password='{1}'
            """.format(
              username.replace("\'", "\'\'"),
              password.replace("\'", "\'\'")
            )
            
    return cur.execute(query).fetchall()
    
  def select_user_by_username(self, username: str) -> list:
    cur = self.__connection.cursor()
    
    query = """
            SELECT *
            FROM users
            WHERE username='{0}'
            """.format(
              username.replace("\'", "\'\'")
            )
    
    return cur.execute(query).fetchall()
