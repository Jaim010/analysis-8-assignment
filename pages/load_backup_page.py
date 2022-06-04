import re
from os import listdir
from getpass import getpass
from zipfile import ZipFile
from pages.page import Page
from datetime import datetime
from utils import logger

class LoadBackupPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
    self.error = None
    self.activity = "Restore form backup"
    
  def display(self) -> None:
    super().display()

    if self.error != None:
      print(self.error + "\n")
      self.error = None
    
    values = listdir("./backups/")
    keys = [i for i in range(1, len(values)+1)]
    mapping = dict(zip(keys, values))

    for key, value in mapping.items():
      posix_time_stamp = re.search("backup-(.*).zip", value).group(1)
      posix_time_stamp = int(posix_time_stamp)
      time_stamp = datetime.fromtimestamp(posix_time_stamp)
      print(
        f"ID: {key}\n" + 
        f"> Backup created on: {time_stamp}\n" + 
        f"> File: {value}\n"
      )
      
    print("Enter backup ID:")
    user_input = input("> ")
    
    if not user_input.isnumeric():
      self.error = "# Invalid input. Input has to be a number. #"
      logger.log(
        activity=self.activity,
        information=f"Invalid input, user entered: {user_input}",
        user=self.controller.user
      )
      return
    
    user_input = int(user_input)
    
    if user_input > keys[-1]:
      self.error = "# Invalid input. Input does not map to a backup. #"
      logger.log(
        activity=self.activity,
        information=f"Invalid input, user entered: {user_input}",
        user=self.controller.user
      )
      return
    
    self.refresh()
    try:
      with ZipFile(f"./backups/{mapping[user_input]}", "r") as zipObj:
        zipObj.extractall("./")
      print("Backup has succesfully been loaded.\n")

      logger_info = f"Restored from backup: {mapping[user_input]}",
      
    except Exception as err:
      print(f"Restoring from backup failed.")
      print(f"Error: {err}")
      
      logger_info = f"Failed to restore from backup. Error: {err}",
      
    logger.log(
      activity=self.activity,
      information=logger_info,
      user=self.controller.user
    )
    
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"
    