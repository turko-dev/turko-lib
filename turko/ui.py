from tkinter import ttk
from tkinter import font
from tkinter import Label as Lb
import numpy as np

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

class Font:
    def __init__(self, name, family=None, size=None, weight=None):
        """
        E.g. font = Font(name, family, size, weight)
        """
        defaultValues = {"family": 'Helvetica', "size":12, "weight":'bold'}
        self.name = name
        if(family == None):self.family = defaultValues['family']
        else: self.family = family
        if(size == None):self.size = defaultValues['size']
        else: self.size = size
        if(weight == None):self.weight = defaultValues['weight']
        else: self.weight = weight
        self.font = font.Font(family=self.family, name=self.name, size=self.size, weight=self.weight)

    def __str__(self):
        return "font"

class Frame:
    def __init__(self, parent, width, height, styleName, bg="#FFFFFF", borderwidth=0):
        
        #Frame Parent & Children Configuration
        self.parent = parent
        self.childCount = 0       
        
        #Frame Content & Item Justification & Alignment
        self.contentJustification = "evenly" #even justification is default
        self.itemAlignment = "center" #center is default
        
        
#Resize Case 1 Binding
        if(isinstance(width, str) and (isinstance(height, int))):
            percentage_string = []
            self.percentage_width = ""
            if '%' in width:
                for x in width: percentage_string.append(x)
            percentage_string.remove('%')
            for y in percentage_string:self.percentage_width += y
            self.pwidth = int(self.percentage_width)
            self.pheight = height
            self.parent.root.bind("<Configure>", self._resize_case_1, add=True)
#Resize Case 2 Binding
        elif(isinstance(height, str) and isinstance(width, int)):
            percentage_string = []
            self.percentage_height = ""
            if '%' in height:
                for x in height: percentage_string.append(x)
            percentage_string.remove('%')
            for y in percentage_string:self.percentage_height += y
            self.pheight = int(self.percentage_height)
            self.pwidth = width
            self.parent.root.bind("<Configure>", self._resize_case_2, add=True)
#Resize Case 3 Binding
        elif(isinstance(width, str) and isinstance(height, str)):
            percentage_string_1, percentage_string_2 = [], []
            self.percentage_height, self.percentage_width = "", ""
            for x in width: percentage_string_1.append(x)
            for y in height: percentage_string_2.append(y)
            percentage_string_1.remove('%')
            percentage_string_2.remove('%')
            for a in percentage_string_1: self.percentage_width += a
            for b in percentage_string_2: self.percentage_height += b
            self.pwidth = int(self.percentage_width)
            self.pheight = int(self.percentage_height)
            self.parent.root.bind("<Configure>", self._resize_case_3, add=True)
#Resize Case 4 Binding
        else:
            self.pwidth = width
            self.pheight = height
            self.parent.root.bind("<Configure>", self._resize_case_4, add=True)


        #Frame Styling
        self.borderWidth = borderwidth
        self.backgroundColor = bg
        frameStyle = ttk.Style()
        frameStyle.configure(f"{styleName}.TFrame", borderwidth=self.borderWidth, background=self.bg, relief="raised") 
        

        #Frame Init
        self.root = ttk.Frame(master=parent.root, width=0, height=0, style=f"{styleName}.TFrame")
        self.root.update_idletasks()
        self.root.pack_propagate(False)
        self.root.pack()
        

    
    #Resize Case 1
    def _resize_case_1(self, event):
        self.width = event.width * (self.pwidth / 100)
        self.height = self.pheight
        if(event.widget == self.parent.root):
            self.root.after(0 ,self.root.config(width=self.width, height=self.height))
    
    #Resize Case 2
    def _resize_case_2(self, event):
        self.width = self.pwidth
        self.height = event.height * (self.pheight / 100)
        if(event.widget == self.parent.root):
            self.root.after(0 ,self.root.config(width=self.width, height=self.height))
    
    #Resize Case 3
    def _resize_case_3(self, event):
        self.width = event.width * (self.pwidth / 100)
        self.height = event.height * (self.pheight / 100)
        if(event.widget == self.parent.root):
            self.root.after(0 ,self.root.config(width=self.width, height=self.height))

    #Resize Case 4
    def _resize_case_4(self, event):
        self._justification = np.round(np.linspace(0, self.pwidth, self.childCount + 2))
        self.root.after(0, self.root.config(width=self.pwidth, height=self.pheight))

    #Return String Format
    def __str__(self):
        return "frame"