from tkinter import font
from tkinter import Label as Lb



class Label:
    def __init__(self, parent, text, x, anchor, fg="#000000"):
        #Let's say the font has a fontSize of 12
        text = text + " "
        self.x = x
        self.anchor = anchor
        #makes accessable to other elements
        if(str(parent) == "frame"): 
            parent.childCount += 1
        self.text = text
        self.fg = fg
        self.bg = parent.backgroundColor
        self.font = font.Font(family="Helvetica", size=12, weight="normal")
        self.label = Lb(parent.root, text=self.text, font=self.font, fg=self.fg, bg=self.bg)
        parent.root.bind("<Configure>", self._resize, add=True)

    def _resize(self, event):
        self.parentWidth = event.width
        self.parentHeight = event.height
        #parent._justification

        """
        Keep working on this
        """
        self.label.place(relx=self.x, rely=0.5, anchor=self.anchor)

    def __str__(self):
        return "label"
