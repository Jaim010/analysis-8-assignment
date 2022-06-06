from getpass import getpass
from pages.page import Page
import utils.validation as validation
import utils.database as database
import utils.logger as logger
from utils.encryption import encrypt
from utils.bcolors import bcolors as bs
import string, random

class ResetUserPasswordPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    print("Please enter the username of the user you want to password reset.")
    username = validation.get_user_input("> Enter the username: ", [validation.is_valid_username()])
    
    authorization_level = self.controller.user.authorization_level
    users = database.execute_query("SELECT * FROM users WHERE username=? AND authorization_level < ?", encrypt(username), authorization_level)
    
    if len(users) == 0:
        print(f"\nNo user exists with the username {username} (or you do not have the permission to update their password)")
        logger.log(
          "Password update", 
          f"\nNo user exists with the username {username} or this user does not have permission to update their password", 
          self.controller.user, 
          False
        )
    else:
        N = 16
        password = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))

        database.execute_query("UPDATE users SET password=?, forced_password_udpate=? WHERE username=?", encrypt(password), 0, encrypt(username))        
        logger.log("Password update", f"The password for {username} has been updated", self.controller.user, False)

        print(f"The new password for '{username}' is '{bs.WARNING}{password}{bs.ENDC}'")

    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   