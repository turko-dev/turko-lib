from tkinter import ttk
import numpy as np

class Frame:
    def __init__(self, parent, width, height, styleName, bg="#FFFFFF", borderwidth=0):
        
        #Frame Parent & Children Configuration
        self.parent = parent
        self.childCount = 0       
        
        #Frame Content & Item Justification & Alignment
        self.contentJustification = "evenly" #even justification is default
        self.itemAlignment = "center" #center is default

        #Styling Configuration

        self.styleName = styleName

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
        frameStyle.configure(f"{self.styleName}.TFrame", borderwidth=self.borderWidth, background=self.backgroundColor, relief="raised") 
        

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

