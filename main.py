# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library
window = Tk()         # Create the application window

window.geometry('350x200')

# Add a label with the text "Hello"
lbl = Label(window, text="Hello", font=("Arial Bold", 50))

# Place the label in the window at 0, 0
lbl.grid(column=0, row=0)

txt = Entry(window,width=10)
txt.grid(column=1, row=0)

chk_state = BooleanVar()
 
chk_state.set(True) 
 
chk = Checkbutton(window, text='Yeet?', var=chk_state)
 
chk.grid(column=2, row=0)

window.mainloop()     # Keep the window open