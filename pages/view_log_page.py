from pages.page import Page
from utils import logger
import utils.logger as logger
from getpass import getpass

class ViewLogPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
   
    encrypted_content = logger.get_log_content()
    decrypted_content = logger.decrypt_log(encrypted_content)
    
    print("Log content: \n")
    for line in decrypted_content:
      print(line)
    
    logger.log(
      activity="Viewing log content",
      information=r"N\A",
      user=self.controller.user
    )
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"