from pages.page import Page
import getpass

class StartPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    
  def display(self) -> None:
    super().display()
    print(
      "Welcome User!" 
      )
    getpass.getpass("> Press enter to continue ...")
    self.controller.next_page = "LoginPage"
    