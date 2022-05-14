import tkinter as tk

from utils.user import User

class MainMenuPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    self.welcome_label = tk.Label(self, font=controller.title_font)
    self.welcome_label.config(text=f"{User().username}")
    self.welcome_label.pack(side="top", fill="x", pady=10)

