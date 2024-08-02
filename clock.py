import sys
from tkinter import *
import time
def timing():
    # strftime means string format time
    current_time = time.strftime("%H : %M : %S")
    # configure the clock
    clock.config(text=current_time)
    # clock will change after every 200 microseconds
    clock.after(100, timing)
# Create a variable that will store our tkinter window
root = Tk()
# define size of the window
root.geometry("600x300")
clock = Label(root, font=("times", 60, "bold"), bg="red")
clock.grid(row=2, column=2, pady=25, padx=100)
timing()
# create a variable for digital clock
a = Label(root, text="Digital Clock!!!!", font="times 30 bold")
a.grid(row=1, column=2)
b= Label(root, text="hours          minutes          seconds", font="times 17 bold")
b.grid(row=3, column=2)
root.mainloop()
