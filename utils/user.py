from datetime import date

class User():
  def __init__(self, first_name, last_name, username, authorization_level, registration_date) -> None:
    self.first_name: str = first_name
    self.last_name: str = last_name
    self.username: str = username
    self.authorization_level: int = authorization_level
    self.registration_date: date = registration_date
