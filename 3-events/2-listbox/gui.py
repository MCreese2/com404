from tkinter import *
from tkinter import messagebox

class Gui(Tk):
    
    def __init__(self):
        super().__init__()
        
        # set window attributes
        self.title("Tickets")
        
        # add components
        self.__add_input_frame()
        self.__add_heading_label()
        self.__add_instruction_label()
        self.__add_lyrics_entry()
        self.__add_add_button()
    

    def __add_heading_label(self):
        self.heading_label = Label()
        self.heading_label.grid(row=0, column=0, columnspan=2)

        self.heading_label.configure( 
            font = "Arial 20",
            text = "Song Maker",
            pady = 5
        )
        
    def __add_instruction_label(self):
        self.message_label = Label()
        self.message_label.grid(row=1, column=0, columnspan=2, sticky = W)
        
        self.message_label.configure( 
            font = "Arial 12",
            text = "Lyric to add:",
            pady = 5
        )
   
    def __add_input_frame(self):
        self.input_frame = Frame()
        self.input_frame.grid(row=2, column=0)

    def __add_lyrics_entry(self):  
        self.entry_box = Entry(self.input_frame)
        self.entry_box.pack(side = LEFT)
        self.entry_box.configure( 
            font = "Arial 12", 
            width = "30"
        )
        
    def __add_add_button(self):
        #create
        self.add_button = Button(self.input_frame)
        self.add_button.pack(side = RIGHT)

        #style
        self.add_button.configure(
            font = "Arial 12", 
            text = "Add",
            width = 10,
            bg = "#f5e9ea",
            activebackground = "#f00",
        )

    def __add_lyric_label(self):
        self.message_label = Label()
        self.message_label.grid(row=3, column=0, columnspan=2, sticky = W)
        
        self.message_label.configure( 
            font = "Arial 12",
            text = "Lyrics:",
            pady = 5
        )

    def __add_lis_box(self):
        self.list_box = Listbox()
        self.list_box.grid(row=4, column=0, columnspan=2)
        
        self.listbox.configure()
        )

        #event
        self.add_button.bind("<ButtonRelease-1>", self.__add_button_clicked)

    def __add_button_clicked(self, event):
        self.entry_box.get()