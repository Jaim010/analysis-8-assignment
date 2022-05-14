from pages.page import Page
from controllers import login

class LoginPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    self.invalid_credentials = False
    
  def display(self) -> None:
    super().display()
    if self.invalid_credentials: 
      print("# Invalid Credentials # \n")
      
    # print("To quit type: !q\n")
    username = input("Username: ")    
    password = input("Password: ")
    
    valid_login = login.login(username, password)
    if valid_login:
      self.invalid_credentials = False
      self.controller.next_page = "MainMenuPage"
    else:
      self.invalid_credentials = True
      self.controller.next_page = "LoginPage"