import json
from utils import Database
from controllers.app import App

if __name__ == "__main__":
  with open("./settings.json") as file:
    settings = json.load(file)
    
  Database().create_connection(settings["database"]["path"])
  
  app = App()