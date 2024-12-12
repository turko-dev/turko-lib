from tkinter import font
from tkinter import Label as Lb



class Label:
    def __init__(self, parent, x, text, fg="#000000"):
        #Let's say the font has a fontSize of 12
        self.parent = parent
        self.x = x
        text = text
        #makes accessable to other elements
        self.childID = None
        if(str(self.parent) == "frame"): 
            self.parent.childCount += 1
            self.childID = parent.childCount
        self.text = text
        self.fg = fg
        self.bg = self.parent.backgroundColor
        self.font = font.Font(family="Helvetica", size=12, weight="normal")
        self.label = Lb(parent.root, text=self.text, font=self.font, fg=self.fg, bg=self.bg)
        parent.root.bind("<Configure>", self._resize, add=True)

    def _resize(self, event):
        self.parentWidth = event.width
        self.parentHeight = event.height
        anchor = "center"
        if(self.childID == 1):anchor = "w"
        elif(self.childID == self.parent.childCount):anchor = "e"
        else:anchor = "center"
        self.parentJustification = self.parent._justification 
        
        if(self.parent.contentJustification == "between"):
            #Visualise the justification board
            
            self.label.place(relx=self.x, rely=0.5, anchor=anchor)
            

            
        elif(self.parent.contentJustification == "evenly"):
            
            self.label.place(relx=self.x, rely=0.5, anchor=anchor)
            

    def __str__(self):
        return "label"
