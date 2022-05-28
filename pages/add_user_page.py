from datetime import date
from getpass import getpass
from pages.page import Page
import utils.database as database
from utils.encryption import encrypt
import utils.validation as validation
import utils.authentication as authentication
import utils.logger as logger

class AddUserPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    print("Please enter the information of the user you want to add.")
    first_name = validation.get_user_input("> Enter their first name: ", [validation.check_length(2, 20)])
    last_name = validation.get_user_input("> Enter their last name: ", [validation.check_length(2, 20)])
    username = validation.get_user_input("> Enter their username: ", [validation.is_valid_username()])
    password = validation.get_user_input("> Enter their password: ", [validation.is_valid_password()])
    
    authorization_level = self.controller.user.authorization_level
    
    for i in range(1, authorization_level):
        authorization_level_name = authentication.to_name(i)
        
        print(f"{i} - {authorization_level_name}")
        
    authorization_level_input = validation.get_user_input("> Enter their role: ", [validation.check_options(range(1, authorization_level))])
    
    database.execute_query(f"INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)", encrypt(first_name), encrypt(last_name), encrypt(username), encrypt(password), authorization_level_input, date.today())
    
    logger.log("Created account", f"Username: {username}, Role: {authentication.to_name(int(authorization_level_input))}", self.controller.user, False)
    print("Created the user.")
    
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   