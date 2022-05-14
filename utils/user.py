from datetime import date
from utils.singleton import Singleton

class User(metaclass=Singleton):
  def __init__(self) -> None:
    self.first_name: str
    self.last_name: str
    self.username: str
    self.authorization_level: int
    self.registration_date: date
    self.reset()
   
  def reset(self):
    self.first_name = None
    self.last_name = None
    self.username = None
    self.authorization_level = None
    self.registration_date = None