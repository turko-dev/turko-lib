from turko import *

turko = Turko()
turko.minsize(200, 200)

frame1 = Frame(turko, width="50%", height="50%", bg="orange", borderwidth=2)

lbl1 = Label(frame1, text="Test", fg="white", x=0, anchor="w")
lbl2 = Label(frame1, text="Test", fg="white", x=1, anchor="e")

frame2 = Frame(turko, width="50%", height="50%", bg="blue", borderwidth=2)
lbl3 = Label(frame2, text="Test", fg="white", x=0, anchor="w")
lbl4 = Label(frame2, text="Test", fg="white", x=1, anchor="e")

turko.run()