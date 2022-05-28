from pages.page import Page
from controllers.login import logout
from utils.user import User

class MainMenuPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
  
  def display(self) -> None:
    super().display()
    print(
      f"Welcome {self.controller.user.username}.\n" +
      "\n" + 
      "1: Update password \n" + 
      "2: List users \n" + 
      "3: Add user \n" +
      "6: Reset user password \n" +
      "\n"
      "To:\n" +
      " > logout type: /lo\n" + 
      " > quit type:   /q\n" 
      )
    
    user_input = input("> ")
    
    if user_input == "/lo":
      logout(self)
      self.controller.next_page = "LoginPage"
    
    if user_input == "/q":
      exit()
    
    if user_input == "1":
      self.controller.next_page = "UpdatePasswordPage"
    if user_input == "2":
      self.controller.next_page = "ListUsersPage"
      
    if self.controller.user.authorization_level > 1:
      if user_input == "3":
        self.controller.next_page = "AddUserPage"
      if user_input == "6":
        self.controller.next_page = "ResetUserPasswordPage"