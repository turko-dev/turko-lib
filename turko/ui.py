from tkinter import ttk
class Frame:
    def __init__(self, parent, width, height):
        self.parent = parent            
        self.frame = ttk.Frame(master=parent.root, width=0, height=0)
        self.parent.root.bind("<Configure>", self.resize, add=True)
        self.frame.pack()
        self.frame.pack_propagate(False)
        


    def resize(self, event):
        self.width = event.width * 0.9
        self.height = event.height * 0.9
        if(event.widget == self.parent.root):
            self.frame.after(5 ,self.frame.config(width=self.width, height=self.height))

#IMPLEMENT AFTER() function somewhere here