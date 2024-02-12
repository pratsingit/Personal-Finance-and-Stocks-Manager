import tkinter as tk

 
from login_page.login import login
from signup_page.signup import signup
from dashboard_page.dashboard import dashboard
from addaccount_page.addaccount import addaccount
from addrevenue_page.addrevenue import addrevenue
from addexpense_page.addexpense import addexpense
from addinvestment_page.addinvestment import addinvestment


class App(tk.Tk):

    def __init__(self, *args, **kwargs):

        tk.Tk.__init__(self, *args, **kwargs)

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}

        for F in (login, signup, addaccount, addrevenue, addexpense, addinvestment):
            page_name = F.__name__
            frame = F(parent = container, controller = self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            
        self.show_frame("addaccount")

    def show_frame(self, page_name):
            frame = self.frames[page_name]
            frame.tkraise()

        
if __name__ == "__main__":
    Application = App()
    Application.mainloop()

