from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    def __init__(self):
        super().__init__()

        #load resources
        self.map_image = PhotoImage(file="2-guis/4-images/3-positioning/map.gif")
        self.ship_image = PhotoImage(file="2-guis/4-images/3-positioning/ship.gif")


        #set window attributes
        self.title("Gui")

        #add components
        self.__add_text_label()
        self.__add_name_label()
        self.__add_name_entry()
        self.__add_name_check()
        self.__add_pport_label()
        self.__add_pport_entry()
        self.__add_pport_check()
        self.__add_check_button()

    def __add_text_label(self):
        
        #create
        self.text_label = Label()
        self.text_label.grid(row = 0, column = 0, columnspan = 3)
        
        #style
        self.text_label.configure(
            text = "Hotel Check In",
            font = "Arial 20",
            pady = 5
        )

    def __add_name_label(self):
        pass

    def __add_name_entry(self):
        pass

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()