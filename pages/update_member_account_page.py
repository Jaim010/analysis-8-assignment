from getpass import getpass
from pages.page import Page
import utils.validation as validation
import utils.database as database
import utils.logger as logger
from utils.encryption import decrypt, encrypt
from utils.bcolors import bcolors as bs
import json

class UpdateMemberAccountPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    print("Please enter the membership id of the member you want to modify.")
    print(f"{bs.WARNING}Note: Membership ID is 10 numbers long{bs.ENDC}")
    membership_id = validation.get_user_input("> Enter the membership ID: ", [validation.is_number(), validation.check_length(10, 10)])
    
    members = database.execute_query("SELECT * FROM members WHERE membership_id=?", membership_id)
    
    if len(members) == 0:
        print(f"\nNo member exists with the specified membership id.")
    else:
        member = members[0]
        first_name, last_name, address, city, email_address, mobile_phone, registration_date, membership_id = member
        first_name, last_name, address, city, email_address, mobile_phone = decrypt(first_name), decrypt(last_name), decrypt(address), decrypt(city), decrypt(email_address), decrypt(mobile_phone)
        
        while True:
            print(""
                + "1: Update first name\n"
                + "2: Update last name\n"
                + "3: Update address\n"
                + "4: Update city\n"
                + "5: Update email address\n"
                + "6: Update mobile phone\n"
                + "7: Go back to the main menu\n"
            )
            
            user_input = validation.get_user_input("> Select an option: ", [validation.check_options(range(1, 8))])
            
            if user_input == "1":
                print(f"Current first name: {first_name}")
                new_firstname = validation.get_user_input("> Enter the new first name: ", [validation.check_length(2, 20)])
            
                database.execute_query("UPDATE members SET first_name=? WHERE membership_id=?", encrypt(new_firstname), membership_id)
                logger.log("Change member first name", f"Changed the first name of member {membership_id} to {new_firstname}", self.controller.user, False)
            if user_input == "2":
                print(f"Current last name: {last_name}")
                new_lastname = validation.get_user_input("> Enter the new last name: ", [validation.check_length(2, 20)])
                
                database.execute_query("UPDATE members SET last_name=? WHERE membership_id=?", encrypt(new_lastname), membership_id)
                logger.log("Change member last name", f"Changed the last name of member {membership_id} to {new_lastname}", self.controller.user, False)
            if user_input == "3":
                print(f"Current address: {address}")
                
                street_name = validation.get_user_input("> Enter their street name: ", [validation.check_length(2, 30)])
                house_number = validation.get_user_input("> Enter their house number: ", [validation.is_number(), validation.check_length(1, 10)])
                zipcode = validation.get_user_input("> Enter their zip code: ", [validation.is_valid_zipcode()])
                new_address = f"{zipcode} {street_name} {house_number}"
                
                database.execute_query("UPDATE members SET address=? WHERE membership_id=?", encrypt(new_address), membership_id)
                logger.log("Change member address", f"Changed the address of member {membership_id} to {new_address}", self.controller.user, False)
            if user_input == "4":
                print(f"Current city: {city}")
                with open("./settings.json") as file:
                    settings = json.load(file)
                
                available_cities = settings["available_cities"]
                print("\nPlease pick a city from the following options: ")
                for available_city in available_cities:
                    print(f"- {available_city}")
                print()
                new_city = validation.get_user_input("> Enter their city: ", [validation.check_length(2, 30), validation.check_options(available_cities)])
                
                database.execute_query("UPDATE members SET city=? WHERE membership_id=?", encrypt(new_city), membership_id)
                logger.log("Change member city", f"Changed the city of member {membership_id} to {new_city}", self.controller.user, False)
            if user_input == "5":
                print(f"Current email address: {email_address}")
                new_email_address = validation.get_user_input("> Enter the new address: ", [validation.is_email()])
                
                database.execute_query("UPDATE members SET email_address=? WHERE membership_id=?", encrypt(new_email_address), membership_id)
                logger.log("Change member email address", f"Changed the email address of member {membership_id} to {new_email_address}", self.controller.user, False)
            if user_input == "6":
                print(f"Current phone number: {mobile_phone}")
                new_mobile_phone = validation.get_user_input("> Enter the new phone number: +31-6-", [validation.is_phone_number()])
                
                database.execute_query("UPDATE members SET mobile_phone=? WHERE membership_id=?", encrypt(new_mobile_phone), membership_id)
                logger.log("Change member mobile_phone", f"Changed the mobile_phone of member {membership_id} to {new_mobile_phone}", self.controller.user, False)
            if user_input == "7":
                break

    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   