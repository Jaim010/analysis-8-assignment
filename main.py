import json
import utils.database as database
from controllers.app import App

if __name__ == "__main__":
  with open("./settings.json") as file:
    settings = json.load(file)
    
  database.create_connection(settings["database"]["path"])
  database.setup()
  
  app = App()

  ## Debug encrypted .log file ##
  # from utils.logger import decrypt_log
  # with open("./.log", "r", encoding="utf-8") as f:
  #   content = f.readlines()
  #   content = decrypt_log(content)
  #   for line in content:
  #     print(line)