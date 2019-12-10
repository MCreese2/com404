from tkinter import *
import time

#the class
class AnimatedGui(Tk):
    def __init__(self):
        super().__init__()

        #load resources
        self.kite_image = PhotoImage(file="2-guis/5-animation/1-single-object/kite.gif")

        #set windows attributes
        self.configure (
            height = 500,
            width = 500
        )

        #set animation attributes
        self.kite_x_pos = 200
        self.kite_y_pos = 0
        self.kite_x_change = 5
        self.kite_y_change = 5

        #add components
        self.add_kite_image_label()

        #start the timer
        self.tick()

    #the timer tick function
    def tick(self):
        if (self.kite_x_pos >= 450) or (self.kite_x_pos <= 0):
            self.kite_x_change = self.kite_x_change * -1

        elif (self.kite_y_pos >= 430) or (self.kite_y_pos < 0):
            self.kite_y_change = self.kite_y_change * -1

        self.kite_x_pos = self.kite_x_pos + self.kite_x_change
        self.kite_y_pos = self.kite_y_pos + self.kite_y_change
        self.kite_image_label.place(
            x=self.kite_x_pos,
            y=self.kite_y_pos
        )
        self.after(100, self.tick)

    #the kite image
    def add_kite_image_label(self):
        self.kite_image_label = Label()
        self.kite_image_label.place(
            x=self.kite_x_pos,
            y=self.kite_y_pos
        )
        self.kite_image_label.configure(image = self.kite_image)

#the object
if __name__ == "__main__":
    gui = AnimatedGui()
    gui.mainloop()