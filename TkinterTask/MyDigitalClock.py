import time
from tkinter import *


class MyDigitalClock:

    def tick(self, time1=""):
        # get the current time from the PC
        time1 = ""
        time2 = time.strftime("%H:%M:%S")
        if time2 != time1:
            time1 = time2
            self.clock.config(text=time2)
        self.clock.after(200, self.tick)

    def __init__(self, root):
        root.title("My DigitalClock")
        img = PhotoImage(file="img/clock.png")
        root.geometry("300x200")
        self.clock = Label(root, font=('arial', 20, 'bold'),
                           bg='black', fg='white')
        self.clock.pack(fill='both', expand=1)
        self.tick()
        root.mainloop()

