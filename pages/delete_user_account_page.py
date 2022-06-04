from getpass import getpass
from pages.page import Page
import utils.validation as validation
import utils.database as database
import utils.logger as logger
from utils.encryption import encrypt

class DeleteUserAccountPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    print("Please enter the username of the user you want to delete.")
    username = validation.get_user_input("> Enter the username: ", [validation.is_valid_username()])
    
    authorization_level = self.controller.user.authorization_level
    users = database.execute_query("SELECT * FROM users WHERE username=? AND authorization_level < ?", encrypt(username), authorization_level)
    
    if len(users) == 0:
        print(f"\nNo user exists with the username {username} (or you do not have the permission to delete their account)")
        logger.log("Member deletion", f"Deletion failed, No user exists with the username {username} or user does not have permission to delete this account", self.controller.user, False)
    else:
        database.execute_query("DELETE FROM users WHERE username=?", encrypt(username))        
        logger.log("Account deletion", f"The account with username {username} has been deleted", self.controller.user, False)

        print(f"The account with the username '{username}' has been deleted")
    
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   