from getpass import getpass
from pages.page import Page
import utils.database as database
import utils.logger as logger
import utils.validation as validation
from utils.bcolors import bcolors as bs
from utils.encryption import encrypt


class ForcedUpdatePasswordPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    self.matching_entries = True
    
  def display(self) -> None:
    super().display()
    
    print(
      f"{bs.WARNING}## Your account's password has recently been reset. ##{bs.ENDC}\n" +
      f"{bs.WARNING}## Please update your password in order to proceed. ##{bs.ENDC}\n"
    )
    
    if not self.matching_entries:
      print(f"{bs.FAIL}# Password entries do not match #{bs.ENDC}")
      self.matching_entries = True
      
    print(
      "Update password:" 
      )
    
    pw_entry = validation.get_user_input("> Enter new password: ", [validation.is_valid_password()])
    pw_second_entry = validation.get_user_input("> Re-Enter new password: ", [validation.is_valid_password()])
    
    if pw_entry == pw_second_entry:
      database.execute_query("UPDATE users SET password=?, forced_password_update=? WHERE username=?", encrypt(pw_entry), 1, encrypt(self.controller.user.username))
      self.controller.user.forced_password_update = 1
      logger.log("Forced password update", f"The password of {self.controller.user.username} has been updated", self.controller.user, False)
      print(
        "\n" +
        "Password succesfully update!"
        "\n"
      )
      getpass("Press enter to continue to the main menu...")
      self.controller.next_page = "MainMenuPage"
    
    else:
      self.matching_entries = False