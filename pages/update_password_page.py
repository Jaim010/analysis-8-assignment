from getpass import getpass
from pages.page import Page
import utils.database as database
import utils.logger as logger
import utils.validation as validation
from utils.user import User
from utils.encryption import encrypt

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
    
    pw_entry = validation.get_user_input("> Enter new password: ", [validation.is_valid_password()])
    pw_second_entry = validation.get_user_input("> Re-Enter new password: ", [validation.is_valid_password()])
    
    if pw_entry == pw_second_entry:
      database.execute_query("UPDATE users SET password=? WHERE username=?", encrypt(pw_entry), encrypt(self.controller.user.username))
      logger.log("Own password update", f"The password of {self.controller.user.username} has been updated", self.controller.user, False)
      print(
        "\n" +
        "Password succesfully update!"
        "\n"
      )
      getpass("Press enter to continue to the main menu...")
      self.controller.next_page = "MainMenuPage"
    
    else:
      self.matching_entries = False
    
   