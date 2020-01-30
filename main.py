# A starter program for Python with Tkinter

from tkinter import * # import Tkinter library

from tkinter import Menu

from tkinter.ttk import Progressbar

from tkinter import ttk

window = Tk()         # Create the application window

menu = Menu(window)
 
new_item = Menu(menu)
 
new_item.add_command(label='New')
 
menu.add_cascade(label='File', menu=new_item)
 
window.config(menu=menu)

window.geometry('365x200')

# Add a label with the text "Hello"
lbl = Label(window, text="Hello", font=("Arial Bold", 50))

# Place the label in the window at 0, 0
lbl.grid(column=0, row=1)
lbl = Label(window, text="Hello")
 
lbl.grid(column=0, row=2)

txt = Entry(window,width=10)

txt.grid(column=1, row=0)

chk_state = BooleanVar()
 
chk_state.set(True) 
 
chk = Checkbutton(window, text='check', var=chk_state)
 
chk.grid(column=2, row=0)

style = ttk.Style()
 
style.theme_use('default')
 
style.configure("black.Horizontal.TProgressbar", background='black')
 
bar = Progressbar(window, length=200, style='black.Horizontal.TProgressbar')
 
bar['value'] = 70
 
bar.grid(column=0, row=0)

btn = Button(window, text="Click Me")
 
btn.grid(column=1, row=1)

btn = Button(window, text="Click Me")
 
btn.grid(column=1, row=2)

window.mainloop()     # Keep the window open