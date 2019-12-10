from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()
        
        #Window Attributes
        #self.geometry("500x250")
        self.title("Currency Converter")
      
        #Window Components
        self.__add_frame()
        self.__add_heading_title()
        self.__add_subheading_title()
        self.__add_input_entry()
        self.__add_button_frame()
        self.__add_clear_button()
        self.__add_convert_button()
        self.__add_message_box()
        self.__add_divider()
        

    def __add_frame(self):
        self.frame = Frame()
        self.frame.pack()
        self.frame.configure(
            pady=10,
            padx=15,
            bg="#ffe8e8"
        )

    def __add_heading_title(self):
        self.heading = Label(self.frame)
        self.heading.grid(row=0, column=0)
        self.heading.configure(
            font = "arial 18",
            text = "Currency Converter",
            bg="#ffe8e8"
        )
    
    def __add_subheading_title(self):
        self.subheading = Label(self.frame)
        self.subheading.grid(row=1, column=0, stick=W)
        self.subheading.configure(
            font = "arial 10",
            text = "Amount",
            bg="#ffe8e8"
        )
    def __add_input_entry(self):
        self.input = Entry(self.frame)
        self.input.grid(row=2, column=0, sticky=W)
        self.input.configure(
            width=60
        )
    
    def __add_button_frame(self):
        self.button_frame = Frame(self.frame)
        self.button_frame.grid(row=3,column=0)
        self.button_frame.configure(
            pady = 20,
            bg="#ffe8e8"
        )

    def __add_clear_button(self):
        self.clear_button = Button(self.button_frame)
        self.clear_button.grid(row=0, column=0, sticky=W)
        self.clear_button.configure(
            text="Clear",
            font="arial 10",
            padx=10
            
        )

        self.clear_button.bind("<ButtonRelease-1>", self.__clear_clicked)

    def __clear_clicked(self, event):
        self.message_box.configure(
            text="System Message Displayed Here"
        )

    def __add_divider(self):
        self.divider = Label(self.button_frame)
        self.divider.grid(row=0, column=1)
        self.divider.configure(
            text="   ",
            bg="#ffe8e8"
        )

    def __add_convert_button(self):

        #Create
        self.convert_button = Button(self.button_frame)
        self.convert_button.grid(row=0, column=2, sticky=E)
        
        #Style
        self.convert_button.configure(
            text="Convert",
            font="arial 10",
            padx=10
        )

        #Event
        self.convert_button.bind("<ButtonRelease-1>", self.__convert_clicked)

    def __convert_clicked(self, event):
        self.message_box.configure(
            text="Converting..."
        )

    def __add_message_box(self):
        self.message_box = Label(self.frame)
        self.message_box.grid(row=4, column=0, stick=N)
        self.message_box.configure(
            width=44,
            height=8,
            bg="#fffbce",
            font="arial 10",
            text="System Message Displayed Here",

        )

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()
