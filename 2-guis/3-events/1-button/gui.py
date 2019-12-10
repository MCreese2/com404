from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_tickets_entry()
        self.__add_buy_button()
        
    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)

        self.heading_label.configure( 
            font = "Arial 20",
            text = "Entrance Ticket",
            pady = 5
        )
        
    def __add_instruction_label(self):
        self.message_label = Label()
        self.message_label.grid(row=1, column=0, columnspan=2)
        
        self.message_label.configure( 
            font = "Arial 12",
            text = "How many tickets are needed?",
            pady = 5
        )
        
    def __add_tickets_entry(self):  
        self.entry_box = Entry()
        self.entry_box.grid(row=3, column=0, padx = 5)

        self.entry_box.configure( 
            font = "Arial 12", 
            width = "30"
        )
        
    def __add_buy_button(self):
        #create
        self.buy_button = Button()
        self.buy_button.grid(row=4, column=0, pady = 10)

        #style
        self.buy_button.configure(
            font = "Arial 12", 
            text = "Buy",
            width = 12,
            bg = "#f5e9ea",
            activebackground = "#f00",
        )

        #event
        self.buy_button.bind("<ButtonRelease-1>", self.__buy_button_clicked)

    def __buy_button_clicked(self, event):
        if  (int(self.entry_box.get()) == 1):
            messagebox.showinfo("Purchased!", "You have purchased 1 ticket!")
        
        elif (int(self.entry_box.get()) > 1):
            messagebox.showinfo("Purchased!", "You have purchased " + self.entry_box.get() + " tickets!")

        else:
            messagebox.showinfo("Error!","Invalid Entry!")

        