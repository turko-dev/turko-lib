from turko import *
from tkinter import ttk

turko = Turko()
turko.minsize(200, 200)
frame = Frame(turko, "50%", 500, styleName="big", bg="green", borderwidth=2)
frame = Frame(frame, 100, 500, styleName="small", bg="orange")

turko.run()