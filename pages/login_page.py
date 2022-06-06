from pages.page import Page
from controllers import login
from utils import validation, logger
from utils.bcolors import bcolors as bs

class LoginPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    self.invalid_credentials = False
    
  def display(self) -> None:
    super().display()
    if self.invalid_credentials: 
      print(f"{bs.FAIL}# Invalid username and/or password #{bs.ENDC}")
      self.invalid_credentials = False
      
    username = validation.get_user_input("Username: ", [validation.is_valid_username()])
    password = validation.get_user_input("Password: ", [validation.is_valid_password()])
    
    valid_login = login.login(self.controller, username, password)
    if valid_login:
      self.controller.next_page = "MainMenuPage"
      logger_info = f"Succes with username: {username}"
      
    else:
      self.invalid_credentials = True
      self.controller.next_page = "LoginPage"
      logger_info = f"Failed with username: {username} | password: {password}"
    
    logger.log(
      activity="Login",
      information=logger_info,
      user=None,
      suspicious= True if login.login_attempts >= 3 else False
    )