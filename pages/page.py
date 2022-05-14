from abc import ABC, abstractmethod

class Page(ABC):
  def __init__(self, controller) -> None:
    self.controller = controller
  
  def display(self) -> None:
    import os
    if(os.name == "posix"):
      os.system("clear")
    else:
      os.system("cls")