from turko import *
turko = Turko()
from tkinter import Canvas
turko.minsize(200, 200)

frame1 = Frame(turko, width="50%", height=500, styleName="frame1", bg="orange", borderwidth=2)
lbl1 = Label(frame1, text="Test", fg="white", x=0, anchor="w")
lbl2 = Label(frame1, text="Test", fg="white", x=1, anchor="e")



turko.run()