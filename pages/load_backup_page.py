from getpass import getpass
from zipfile import ZipFile
from pages.page import Page
from os import listdir

class LoadBackupPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    self.error = None
    
  def display(self) -> None:
    super().display()

    if self.error != None:
      print(self.error + "\n")
      self.error = None
    
    values = listdir("./backups/")
    keys = [i for i in range(1, len(values)+1)]
    mapping = dict(zip(keys, values))

    for key, value in mapping.items():
      print(f"{key}: {value}")
      
    print()
    user_input = input("> ")
    
    if not user_input.isnumeric():
      self.error = "# Invalid input. Input has to be a number. #"
      return
    
    user_input = int(user_input)
    
    if user_input > keys[-1]:
      self.error = "# Invalid input. Input does not map to a backup. #"
      return
    
    self.refresh()
    try:
      with ZipFile(f"./backups/{mapping[user_input]}", "r") as zipObj:
        zipObj.extractall("./")
      print("Backup has succesfully been loaded.\n")
    except Exception as err:
      print(err)
    
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    