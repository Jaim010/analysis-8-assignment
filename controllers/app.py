from pages import *

class App:
  def __init__(self) -> None:
    self.pages = {}
    for PAGE in (StartPage, LoginPage, MainMenuPage, UpdatePasswordPage):
      page_name = PAGE.__name__
      page = PAGE(controller=self)
      self.pages[page_name] = page

    self.next_page = "StartPage"
    self.show_page()
    
  def show_page(self):
    '''Show a frame for the given page name'''
    while not self.next_page == None:
      page = self.pages[self.next_page]
      page.display()