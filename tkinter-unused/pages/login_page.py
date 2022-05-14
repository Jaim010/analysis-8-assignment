import tkinter as tk
from controllers.login import login
from utils.user import User

class LoginPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller

    usernameLabel = tk.Label(self, text="User Name").grid(row=0, column=0)
    username = tk.StringVar()
    usernameEntry = tk.Entry(self, textvariable=username).grid(row=0, column=1)  

    passwordLabel = tk.Label(self, text="Password").grid(row=1, column=0)  
    password = tk.StringVar()
    passwordEntry = tk.Entry(self, textvariable=password, show='*').grid(row=1, column=1)  
    
    loginButton = tk.Button(self, text="Login", 
                            command=lambda: self.submit(username.get(), password.get())
                            ).grid(row=4, column=0) 
    
    # if valid login && switch frame
    # else show error message
      
  def submit(self, username, password):
    if login(username, password):
      self.controller.frames["MainMenuPage"].welcome_label.config(text=f"{User().username}")
      self.controller.show_frame("MainMenuPage") 
    else:
      self.controller.show_frame("InvalidLoginPage")