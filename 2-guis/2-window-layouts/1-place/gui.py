from tkinter import *

# the Gui class inherits from Tk
class Gui(Tk):
    def __init__(self):
        super().__init__()

        # set window attributes
        self.geometry("500x250")
        self.title("Newsletter")
        self.configure(bg="#eee",)

        # add window compenents
        self.__add_heading_label()
        self.__add_message_label()
        self.__add_email_label()
        self.__add_entry_box()
        self.__add_submit_button()

    def __add_heading_label(self):
        # create
        self.heading_label = Label()
        self.heading_label.place(x=60, y=40)
        # style
        self.heading_label.configure( font = "Arial 20",
                                      text = "RECEIVE OUR NEWSLETTER")
        # events

    def __add_message_label(self):
          # create
        self.message_label = Label()
        self.message_label.place(x=60, y=100)
        # style
        self.message_label.configure( font = "Arial 12",
                                      text = "Please enter your email below to receive our newsletter.")
        # events

    def __add_email_label(self):
        # create
        self.email_label = Label()
        self.email_label.place(x=80, y=160)
        # style
        self.email_label.configure( font = "Arial 12",
                                    text = "Email:")
        # events
        
    def __add_entry_box(self):
        # create
        self.entry_box = Entry()
        self.entry_box.place(x=135, y=160)
        # style
        self.entry_box.configure( font = "Arial 12", 
                                  width = "30")
        
        # events

    def __add_submit_button(self):
        # create
        self.submit_button = Button()
        self.submit_button.place(x=0, y=220)
        # style
        self.submit_button.configure( font = "Arial 12", 
                                      text = "Subscribe",
                                      width = 55,
                                      bg = "#f5e9ea",
                                      activebackground = "#f00")
        
        # events






# "pass" can be used as a placeholder