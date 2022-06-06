from dataclasses import dataclass
from datetime import date

@dataclass
class User:
  first_name: str 
  last_name: str 
  username: str 
  authorization_level: int 
  registration_date: date 
  forced_password_udpate: int
  
  @property
  def forced_password_udpate(self):
    return self._forced_password_udpate == 0
  
  @forced_password_udpate.setter
  def forced_password_udpate(self, value):
    if value in (0, 1):
      self._forced_password_udpate = value
    else:
      raise Exception(f"Expected value between 0 or 1. Given: {value}")