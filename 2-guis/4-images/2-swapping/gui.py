from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        #load resources
        self.cactus_image = PhotoImage(file="2-guis/4-images/2-swapping/cactus.gif")
        self.cactus_name_image = PhotoImage(file="2-guis/4-images/2-swapping/cactus-with-name.gif")


        #set window attributes
        self.title("Gui")

        #add components
        self.__add_text_label()
        self.__add_cactus_image_label()
        self.__add_swap_button()

    def __add_text_label(self):
        
        #create
        self.text_label = Label()
        self.text_label.grid(row = 0, column = 0)
        
        #style
        self.text_label.configure(
            text = "Cactus Leaves",
            font = "Arial 20",
            pady = 5
        )

    def __add_cactus_image_label(self):
        self.cactus_image_label = Label()
        self.cactus_image_label.grid(row=1, column=0)
        self.cactus_image_label.configure(
            image=self.cactus_image,
            height=478,
            width=800
        )

    def __add_swap_button(self):
        self.swap_button = Button()
        self.swap_button.grid(row=3, column=0)

        self.swap_button.configure(
            font = "Arial 12", 
            text = "Flip",
            width = 12,
            bg = "#f5e9ea",
            activebackground = "#f00",
        )

        self.swap_button.bind("<ButtonRelease-1>", self.__swap_button_left)
        self.swap_button.bind("<ButtonRelease-3>", self.__swap_button_right)

    def __swap_button_left(self, event):
        self.cactus_image_label.configure(image = self.cactus_name_image)

    def __swap_button_right(self, event):
        self.cactus_image_label.configure(image = self.cactus_image)


if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()