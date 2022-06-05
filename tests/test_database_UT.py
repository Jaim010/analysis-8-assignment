import unittest
from utils import database

class TestDatabase(unittest.TestCase):
  def test_sql_injections(self):
    db_setup()
    
    database.execute_query("INSERT INTO users (username) VALUES ('admin')")
    
    with open("./tests/test_cases.txt", "r") as f:
      test_cases = f.readlines()

    for test in test_cases:
      result = database.execute_query("SELECT * FROM users WHERE username=?", test)
      self.assertEqual(0, len(result))
      
    database.execute_query("DELETE FROM users WHERE username='admin'")
      
  def test_execute_query_given_simple_username(self):
    db_setup()
    username = "admin"
    
    database.execute_query("INSERT INTO users (username) VALUES (?)", username)
    
    result = database.execute_query("SELECT username FROM users WHERE username=?", username)
    
    self.assertEqual(1, len(result))
    self.assertEqual(username, result[0][0])
    
    database.execute_query("DELETE FROM users WHERE username=?", username)
    
    
  def test_execute_query_given_complex_username(self):
    db_setup()
    username = "John O'Conner"
    
    database.execute_query("INSERT INTO users (username) VALUES (?)", username)
    
    result = database.execute_query("SELECT username FROM users WHERE username=?", username)
    self.assertEqual(1, len(result))
    self.assertEqual(username, result[0][0])
    
    database.execute_query("DELETE FROM users WHERE username=?", username)
    

def db_setup():
  db_path = "./tests/test.sqlite"
  
  database.create_connection(db_path)
  database.setup()