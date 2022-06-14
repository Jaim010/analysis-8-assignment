from getpass import getpass
from pages.page import Page
from utils import logger
import utils.database as database
from utils.encryption import decrypt
import utils.authentication as authentication

class ListUsersPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    users = database.execute_query("SELECT * FROM users")
    assert users != None
    print("All users:\n")
    for user in users:
        first_name, last_name, username, _, authorization_level, _, _ = user
        first_name, last_name, username = decrypt(first_name), decrypt(last_name), decrypt(username)
        
        authorization_level_name = authentication.to_name(authorization_level)
        
        print(""
            + "======\n"
            + f"Name: {first_name} {last_name}\n"
            + f"Info: {username} ({authorization_level_name})\n"
        )
    
    logger.log(
      activity="Listed all users",
      information=r"N/A",
      user=self.controller.user
    )
    
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   