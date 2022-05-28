from pages.page import Page
from controllers import login
import utils.validation as validation

class LoginPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    self.invalid_credentials = False
    
  def display(self) -> None:
    super().display()
    if self.invalid_credentials: 
      print("# Invalid Credentials # \n")
      self.invalid_credentials = False
      
    # print("To quit type: !q\n")
    username = validation.get_user_input("Username: ", [validation.is_valid_username()])
    password = validation.get_user_input("Password: ", [validation.is_valid_password()])
    
    valid_login = login.login(self.controller, username, password)
    if valid_login:
      self.controller.next_page = "MainMenuPage"
    else:
      self.invalid_credentials = True
      self.controller.next_page = "LoginPage"