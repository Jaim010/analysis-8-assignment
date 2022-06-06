from getpass import getpass
from pages.page import Page
from utils import database, validation, logger
from utils.encryption import decrypt

class SearchMemberPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    
    print("Enter the search information of the member you want to find.")
    query = validation.get_user_input("> Please enter the member information: ", [validation.check_length(1, 40)]).lower()
    
    members = database.execute_query("SELECT * FROM members")
    
    for member in members:
        first_name, last_name, address, city, email_address, mobile_phone, registration_date, membership_id = member
        first_name, last_name, address, city, email_address, mobile_phone = decrypt(first_name), decrypt(last_name), decrypt(address), decrypt(city), decrypt(email_address), decrypt(mobile_phone)
        
        data = first_name, last_name, address, city, email_address, mobile_phone, registration_date, membership_id
        
        for d in data:
            if query in str(d).lower():
                print("===========")
                print(f"Name: {first_name} {last_name}")
                print(f"Location: {address} {city}")
                print(f"Email: {email_address}")
                print(f"Phone number: +31-6-{mobile_phone}")
                print(f"Membership id: {membership_id}")
                print()
                
                break
    
    logger.log(
      activity="Searching for members",
      information=f"Search query parameter: {query}",
      user=self.controller.user,
    )
    
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    
   