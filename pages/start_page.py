from pages.page import Page
from getpass import getpass
from utils import logger

class StartPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    logger.log(
      activity="Start page",
      information="N\A",
      user="System"
    )
    
    print(
      "Welcome User!" 
      )
    
    getpass("> Press enter to continue ...")
    self.controller.next_page = "LoginPage"
    
    