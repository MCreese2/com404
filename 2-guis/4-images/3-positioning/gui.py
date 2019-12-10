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
        self.__add_map_frame()
        self.__add_map_label()
        self.__add_ship_label()

    def __add_text_label(self):
        
        #create
        self.text_label = Label()
        self.text_label.grid(row = 0, column = 0)
        
        #style
        self.text_label.configure(
            text = "Find the treasure...",
            font = "Arial 20",
            pady = 5
        )

    def __add_map_frame(self):
        self.map_frame = Frame()
        self.map_frame.grid(row=1, column=0)
        self.map_frame.configure(
            width=1200,
            height=927
        )

    def __add_map_label(self):
        self.map_image_label = Label(self.map_frame)
        self.map_image_label.place(x=0, y=0)
        self.map_image_label.configure(
            image=self.map_image,
            width=1200,
            height=927
        )

    def __add_ship_label(self):
        self.ship_image_label = Label(self.map_frame)
        self.ship_image_label.place(x=0, y=0)
        self.ship_image_label.configure(
            image=self.ship_image,
            width=125,
            height=130
        )

        self.ship_image_label.bind("<B1-Motion>", self.__callback)

    def __callback(self, event):
        #messagebox.showinfo("Bus Journey Gui", "Mouse x is " + str(event.x))
        #messagebox.showinfo("Bus Journey Gui", "Mouse y is " + str(event.y))
        self.ship_image_label.place(
            x=event.x,
            y=event.y
        )

   
if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()