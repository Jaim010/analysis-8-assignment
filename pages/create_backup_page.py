from getpass import getpass
import time
from pages.page import Page
from utils import backup, logger

class CreateBackupPage(Page):
  def __init__(self, controller) -> None:
    super().__init__(controller)
  
  def display(self) -> None:
    super().display()
    
    posix_now = round(time.time())
    filename = f"backup-{posix_now}"
    
    (succes, err) = backup.create(filename)
    
    if succes:
      print(
        "Zip file has been created:\n" + 
        f" - With name: {filename}.zip\n" +
        f" - In folder: /backups/\n" 
      )
      act="[Succes] Created backup"
      info=f"Created backup with name /backups/{filename}.zip"

    else:    
      print("[Error] Something went wrong whilst creating the zip file...")
      act = "[Failure] Failed to create backup"
      info = err
    
    logger.log(
      activity=act,
      information=info,
      user=self.controller.user
    )
    getpass("Press enter to continue to the main menu...")
    self.controller.next_page = "MainMenuPage"