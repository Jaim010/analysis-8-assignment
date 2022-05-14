import tkinter as tk
from utils.database import select_user_by_username

class QueryTestPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    
    usernameLabel = tk.Label(self, text="User Name").grid(row=0, column=0)
    username = tk.StringVar()
    usernameEntry = tk.Entry(self, textvariable=username).grid(row=0, column=1)  
    
    select_user_by_username(username.get())