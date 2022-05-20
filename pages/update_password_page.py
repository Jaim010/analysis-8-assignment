from getpass import getpass
from pages.page import Page
import utils.database as database
from utils.user import User

class UpdatePasswordPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    self.matching_entries = True
    
  def display(self) -> None:
    super().display()
    
    if not self.matching_entries:
      print("# Password entries do not match #")
      self.matching_entries = True
      
    print(
      "Update password:" 
      )
    
    pw_entry = input("> Enter new password: ")
    pw_second_entry = input("> Re-enter new password: ")
    
    if pw_entry == pw_second_entry:
      database.execute_query("UPDATE TABLE user WHERE username='?' AND password='?'", self.controller.user.username, pw_entry)
      print(
        "\n" +
        "Password succesfully update!"
        "\n"
      )
      getpass("Press enter to continue to the main menu...")
      self.controller.next_page = "MainMenuPage"
    
    else:
      self.matching_entries = False
    
   