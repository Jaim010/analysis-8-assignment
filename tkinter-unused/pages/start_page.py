import tkinter as tk

class StartPage(tk.Frame):
  def __init__(self, parent, controller):
    tk.Frame.__init__(self, parent)
    self.controller = controller
    label = tk.Label(self, text="Welcome user!", font=controller.title_font)
    label.pack(side="top", fill="x", pady=10)

    button1 = tk.Button(self, text="Go to Login",
                        command=lambda: controller.show_frame("LoginPage"))
    button1.pack()
