from turko import *

turko = Turko()
turko.minsize(200, 200)

frame1 = Frame(turko, width="50%", height="50%", styleName="frame1", bg="green", borderwidth=2)

frame2 = Frame(frame1, width="95%", height="95%", styleName="frame2", bg="orange", borderwidth=2)

turko.run()
