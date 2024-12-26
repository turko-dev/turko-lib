from turko import *

turko = Turko()
turko.minsize(200, 200)

frame1 = Frame(turko, width="50%", height="50%", bg="orange", borderwidth=2)

lbl1 = Label(frame1, text="Test", fg="white", x=0)
lbl3 = Label(frame1, text="Test", fg="white", x=0.5)
lbl2 = Label(frame1, text="Test", fg="white", x=1)

#Merth Commit

"""
If there are 3 children in the frame
there are 5 numbers in the justification board to
take into account

0 
171 / 683
342 / 683
512 / 683
1

these numbers are all relative to the width
of the parent frame.


"""

turko.run()