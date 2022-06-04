from dataclasses import dataclass
from datetime import date

@dataclass
class User():
  first_name: str 
  last_name: str 
  username: str 
  authorization_level: int 
  registration_date: date 
