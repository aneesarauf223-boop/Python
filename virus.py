# import necessary libraries
from tkinter import *
from tkinter import messagebox
#setup Tkinter window
root = Tk()
root.geometry("200x200")
#function for Displaying warning Message
#this will be called once the button is clicked
#messagebox.showwarming("Alert", "stop! virus Found.")
def msg():
    messagebox.showwarning("Alert", "stop! virus Founs.")
# Adding button wigid to window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)
# Entering main event loop
root.mainloop()