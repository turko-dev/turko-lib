from tkinter import ttk
class Frame:
    def __init__(self, parent, width, height):
        self.parent = parent
        self.frame = ttk.Frame(master=parent.root, width=width, height=height)
        self.parent.root.bind("<Configure>", self.test, add=True)
        self.frame.pack_propagate(True)
        self.frame.pack()

    def test(self, event):
        self.frame.config(width=event.width * 0.9, height=event.height * 0.9)

#IMPLEMENT AFTER() function somewhere here