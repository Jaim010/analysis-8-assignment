import os
import unittest
from utils import database

class TestDatabase(unittest.TestCase):
  def test_execute_query_given_simple_username(self):
    username = "admin"
    
    result = database.execute_query("SELECT username FROM users WHERE username=?", username)
    
    self.assertEqual(1, len(result))
    self.assertEqual(username, result[0][0])
    
    
  def test_execute_query_given_complex_username(self):
    username = "John O'Conner"
    
    database.execute_query("INSERT INTO users (username) VALUES (?)", username)
    
    result = database.execute_query("SELECT username FROM users WHERE username=?", username)
    self.assertEqual(1, len(result))
    self.assertEqual(username, result[0][0])
    
    database.execute_query("DELETE FROM users WHERE username=?", username)
    

def create_test_func(query_param):
  def test_sql_injections(self):
    with open("./tests/test_cases.txt", "r") as f:
      test_cases = f.readlines()

    for test in test_cases:
      result = database.execute_query("SELECT * FROM users WHERE username=?", query_param)
      self.assertEqual(0, len(result))
  return test_sql_injections


# Reads test cases
with open("./tests/test_cases.txt", "r") as f:
  test_cases = f.readlines()

# Adds test case functions to the TestDatabase class
for i, (case) in enumerate(test_cases):
  setattr(TestDatabase, 'test_data_%d'%i, create_test_func(case))


# Prepare a fresh database for testing
db_path = "./tests/test.sqlite"

if os.path.exists(db_path):
  os.remove(db_path)

database.create_connection(db_path)
database.setup()

database.execute_query("DELETE FROM users WHERE username='admin'")
result = database.execute_query("SELECT username FROM users WHERE username=?", "admin")
if (len(result) == 0):
  database.execute_query("INSERT INTO users (username) VALUES (?)", "admin")