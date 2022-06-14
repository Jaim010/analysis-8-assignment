from getpass import getpass
from pages.page import Page
import utils.validation as validation
import utils.database as database
import utils.logger as logger
from utils.encryption import decrypt, encrypt

class UpdateUserAccountPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    print("Please enter the username of the user you want to modify.")
    username = validation.get_user_input("> Enter the username: ", [validation.is_valid_username()])
    
    authorization_level = self.controller.user.authorization_level
    users = database.execute_query("SELECT * FROM users WHERE username=? AND authorization_level < ?", encrypt(username), authorization_level)
    
    if len(users) == 0:
        print(f"\nNo user exists with the username {username} (or you do not have the permission to update their information)")
    else:
        user = users[0]
        first_name, last_name, current_username, _, authorization_level, _, _ = user
        first_name, last_name, current_username = decrypt(first_name), decrypt(last_name), decrypt(current_username)
        
        while True:
            print(""
                + "1: Update username\n"
                + "2: Update first name\n"
                + "3: Update last name\n"
                + "4: Go back to the main menu\n"
            )
            
            user_input = validation.get_user_input("> Select an option: ", [validation.check_options(range(1, 5))])
            
            if user_input == "1":
                print(f"Current username: {current_username}")
                new_username = validation.get_user_input("> Enter the new username: ", [validation.is_valid_username()])
            
                database.execute_query("UPDATE users SET username=? WHERE username=?", encrypt(new_username), encrypt(username))
                logger.log("Change username", f"Changed the username of {username} to {new_username}", self.controller.user, False)
            if user_input == "2":
                print(f"Current first name: {first_name}")
                new_firstname = validation.get_user_input("> Enter the new first name: ", [validation.check_length(2, 20)])
            
                database.execute_query("UPDATE users SET first_name=? WHERE username=?", encrypt(new_firstname), encrypt(username))
                logger.log("Change first name", f"Changed the first name of {username} to {new_firstname}", self.controller.user, False)
            if user_input == "3":
                print(f"Current last name: {last_name}")
                new_lastname = validation.get_user_input("> Enter the new last name: ", [validation.check_length(2, 20)])
                
                database.execute_query("UPDATE users SET last_name=? WHERE username=?", encrypt(new_lastname), encrypt(username))
                logger.log("Change last name", f"Changed the last name of {username} to {new_lastname}", self.controller.user, False)
            if user_input == "4":
                break

    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   