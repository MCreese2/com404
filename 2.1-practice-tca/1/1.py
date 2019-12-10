from tkinter import *

# the Gui class inherits from Tk
class Gui(Tk):
    def __init__(self):
        super().__init__()

        # set window attributes
        #self.geometry("500x250")
        self.title("Newsletter")
        self.configure(bg="#eee",)

        # add window compenents
        self.add_border_frame()
        self.add_frame()
        self.__add_heading_label()
        self.__add_message_label()
        self.add_email_frame()
        self.__add_email_label()
        self.__add_entry_box()
        self.__add_submit_button()
        
    def add_border_frame(self):
        self.border = Frame()
        self.border.pack()
        self.border.configure(
            bd = 10,
            bg = "#878787")

    def add_frame(self):
        self.frame = Frame(self.border)
        self.frame.pack()
        self.frame.configure(bg="#eee")

    def __add_heading_label(self):
        # create
        self.heading_label = Label(self.frame)
        self.heading_label.grid(row=0, column=0, columnspan=2)
        # style
        self.heading_label.configure( font = "Arial 20",
                                      text = "RECEIVE OUR NEWSLETTER",
                                      pady = 10)
        # events

    def __add_message_label(self):
          # create
        self.message_label = Label(self.frame)
        self.message_label.grid(row=1, column=0, columnspan=2)
        # style
        self.message_label.configure( font = "Arial 12",
                                      text = "Please enter your email below to receive our newsletter.",
                                      pady = 5)
        # events

    def add_email_frame(self):
        self.email_frame = Frame(self.frame)
        self.email_frame.grid(row=2, column = 0, columnspan=2)
        self.email_frame.configure(pady = 15)

    def __add_email_label(self):
        # create
        self.email_label = Label(self.email_frame)
        self.email_label.grid(row=0, column=0)
        # style
        self.email_label.configure( font = "Arial 12",
                                    text = "Email:")
        # events
        
    def __add_entry_box(self):
        # create
        self.entry_box = Entry(self.email_frame)
        self.entry_box.grid(row=0, column=1)
        # style
        self.entry_box.configure( font = "Arial 12", 
                                  width = "30")
        
        # events

    def __add_submit_button(self):
        # create
        self.submit_button = Button(self.frame)
        self.submit_button.grid(row=3, column=0, columnspan=2)
        # style
        self.submit_button.configure( font = "Arial 12", 
                                      text = "Subscribe",
                                      width = 55,
                                      bg = "#f5e9ea",
                                      activebackground = "#f00")
        

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()