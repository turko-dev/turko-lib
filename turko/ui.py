from tkinter import YES, ttk
from tkinter import font
from tkinter import Canvas

class Label:
    def __init__(self, parent, text, fg="#000000"):

        textStringLength = len(text)
        print(textStringLength)

        #Let's say the font has a fontSize of 12
        widthLetter = 17.5
        self.bg = parent.backgroundColor
        self.font = font.Font(family="Helvetica", size=12, weight="normal")
        
        self.label = Canvas(parent.root, width=self.font.measure(text), height=20, highlightthickness=0, background=self.bg)
        self.label.create_text((self.font.measure(text) / 2), 10, text=text, fill=fg, font=self.font)
        
        self.label.pack()

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
        return f"<turko.Font(name=\"{self.name}\", family=\"{self.family}\", size={self.size}, weight=\"{self.weight}\")"

class Frame:
    def __init__(self, parent, width, height, backgroundColor):
        """
        there are only 4 cases
        #1 - only width is percentage (100%, 500px)
        #2 - only height is percentage (500px, 100%)
        #3 - both width and height is percentage (100%, 50%)
        #4 - non are percentage (500px, 500px)
        """
        #Type Validation
        if not (isinstance(width, str) or isinstance(width, int)): raise TypeError("width attribute must be either a string percentage or a integer pixel value such as \"100%\" or 100")
        if not (isinstance(height, str) or isinstance(height, int)): raise TypeError("height attribute must be either a string percentage or a integer pixel value such as \"100%\" or 100")
        if not (isinstance(backgroundColor, str)): raise TypeError("backgroundColor attribute must be a string such as \"#FFFFFF\"")
        self.parent = parent
        
        #Styling
        s = ttk.Style()
        self.backgroundColor = backgroundColor
        s.configure('TFrame', background=backgroundColor)
        self.root = ttk.Frame(master=parent.root, width=0, height=0, style='TFrame')

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

        else:
            self.pwidth = width
            self.pheight = height
            self.root.config(width=self.pwidth, height=self.pheight)
        
        self.root.pack()
        self.root.pack_propagate(False)


    
    def _resize_case_1(self, event):
        self.width = event.width * (self.pwidth / 100)
        self.height = self.pheight
        if(event.widget == self.parent.root):
            self.root.after(0 ,self.root.config(width=self.width, height=self.height))
    def _resize_case_2(self, event):
        self.width = self.pwidth
        self.height = event.height * (self.pheight / 100)
        if(event.widget == self.parent.root):
            self.root.after(0 ,self.root.config(width=self.width, height=self.height))
    
    def _resize_case_3(self, event):
        self.width = event.width * (self.pwidth / 100)
        self.height = event.height * (self.pheight / 100)
        if(event.widget == self.parent.root):
            self.root.after(0 ,self.root.config(width=self.width, height=self.height))
