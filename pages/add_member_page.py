from datetime import datetime
from getpass import getpass
from pages.page import Page
import utils.database as database
from utils.encryption import encrypt
import utils.validation as validation
import utils.logger as logger
import random

class AddMemberPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    print("Please enter the information of the member you want to add.")
    first_name = validation.get_user_input("> Enter their first name: ", [validation.check_length(2, 20)])
    last_name = validation.get_user_input("> Enter their last name: ", [validation.check_length(2, 20)])
    
    address = validation.get_user_input("> Enter their address: ", [validation.check_length(2, 30)])
    city = validation.get_user_input("> Enter their city: ", [validation.check_length(2, 30)])
    
    email = validation.get_user_input("> Enter their email: ", [validation.is_email()])
    phonenumber = validation.get_user_input("> Enter their phone number: +31-6-", [validation.is_phone_number()])
    
    membership_id = "" + str(random.randint(1, 9))
    for _ in range(1, 9):
      membership_id += str(random.randint(0, 9))

    total = 0
    for char in membership_id:
      total += int(char)

    membership_id += str(total % 10)
    
    database.execute_query(f"INSERT INTO members VALUES (?, ?, ?, ?, ?, ?, ?, ?)", encrypt(first_name), encrypt(last_name), encrypt(address), encrypt(city), encrypt(email), encrypt(phonenumber), str(datetime.now()), membership_id)
    logger.log("Added member", f"Added member {first_name} {last_name}", self.controller.user, False)
    
    print("Added the member to the database.")
    
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   