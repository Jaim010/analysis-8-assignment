# 1008138 - Thomas Poelman
# 0950044 - Jamey Schaap

import json
import utils.database as database
from controllers.app import App

if __name__ == "__main__":
  with open("./settings.json") as file:
    settings = json.load(file)
    
  database.create_connection(settings["database"]["path"])
  database.setup()
  
  app = App()
