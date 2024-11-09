from tkinter import ttk
class Frame:
    def __init__(self, parent, width, height):
        
        self.parent = parent
        self.frame = ttk.Frame(master=parent.root, width=width, height=height)
        self.parent.root.bind("<Configure>", self.test, add=True)
        self.frame.config(width=100, height=100)
        self.frame.pack()
        self.frame.pack_propagate(False)



    def test(self, event):
        self.width = event.width * 0.9
        self.height = event.height * 0.9
        print(event)
        if(event.widget == self.parent.root):
            self.frame.after(5 ,self.frame.config(width=self.width, height=self.height))

#IMPLEMENT AFTER() function somewhere here