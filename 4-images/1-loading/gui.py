from tkinter import *

class Gui(Tk):
    def __init__(self):
        super().__init__()

        #load resources
        self.ambulance_image = PhotoImage(file="4-images/1-loading/ambulance.gif")
        self.bike_image = PhotoImage(file="4-images/1-loading/bike.gif")
        self.plane_image = PhotoImage(file="4-images/1-loading/plane.gif")

        #set window attributes
        self.title("Gui")

        #add components
        self.__add_text_label()
        self.__add_ambulance_image_label()
        self.__add_bike_image_label()
        self.__add_plane_image_label()

    def __add_text_label(self):
        
        #create
        self.text_label = Label()
        self.text_label.grid(row = 0, column = 0, columnspan = 3)
        
        #style
        self.text_label.configure(
            text = "TRANSPORT",
            font = "Arial 20",
            pady = 5
        )

    def __add_ambulance_image_label(self):
        self.ambulance_image_label = Label()
        self.ambulance_image_label.grid(row=1, column=0)
        self.ambulance_image_label.configure(
            image=self.ambulance_image,
            height=60,
            width=60
        )

    def __add_bike_image_label(self):
        self.ambulance_bike_label = Label()
        self.ambulance_bike_label.grid(row=1, column=1)
        self.ambulance_bike_label.configure(
            image=self.bike_image,
            height=60,
            width=60
        )

    def __add_plane_image_label(self):
        self.ambulance_plane_label = Label()
        self.ambulance_plane_label.grid(row=1, column=2)
        self.ambulance_plane_label.configure(
            image=self.plane_image,
            height=60,
            width=60
        )

if (__name__ == "__main__"):
    gui = Gui()
    gui.mainloop()