from pages.page import Page
from controllers.login import logout
from utils import user
from utils.user import User

class MainMenuPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
  
  def display(self) -> None:
    super().display()
    print(
      f"Welcome {self.controller.user.username}.\n" +
      "\n" + 
      "1: Update my password \n" + 
      "2: Add new member \n" +
      "3: Update member account \n" +
      "4: Search member details"
    )
    
    if self.controller.user.authorization_level > 1:
      print(   
        "5: Delete member account \n" +    
        "6: List users \n" + 
        "7: Add user \n" +
        "8: Update user account \n" +
        "9: Delete user account \n" +
        "10: Reset user password \n" +
        "11: View logs \n" +
        "12: Create backup \n" +
        "13: Load backup \n"
      )
    
    print(
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
      self.controller.next_page = "AddMemberPage"
    if user_input == "3":
      self.controller.next_page = "UpdateMemberAccountPage"
    if user_input == "4":
      self.controller.next_page = "SearchMemberPage"  
      
    if self.controller.user.authorization_level > 1:
      if user_input == "5":
        self.controller.next_page = "DeleteMemberAccountPage"
      if user_input == "6":
        self.controller.next_page = "ListUsersPage"
      if user_input == "7":
        self.controller.next_page = "AddUserPage"
      if user_input == "8":
        self.controller.next_page = "UpdateUserAccountPage"
      if user_input == "9":
        self.controller.next_page = "DeleteUserAccountPage"
      if user_input == "10":
        self.controller.next_page = "ResetUserPasswordPage"
      if user_input == "11":
        self.controller.next_page = "ViewLogPage"
      if user_input == "12":
        self.controller.next_page = "CreateBackupPage"
      if user_input == "13":
        self.controller.next_page = "LoadBackupPage"
