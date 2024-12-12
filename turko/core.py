import tkinter as tk
from screeninfo import get_monitors

class Turko:
    def __init__(self):
        """
        Initialise Core Turko App
        ---------------------------------
        E.g. turko = Turko()

        - initframe will initialise a base frame for the app to load
        - framepadding will give initframe a padding
        """
        self.root = tk.Tk()
        self.root.title("Turko App")
        self.root.attributes("-zoomed", True)
        self.frameCount = 0
        self.width = 0
        self.height = 0
        self.root.bind("<Configure>", self.setgeometry)

    def setgeometry(self, event):
        if(event.widget == self.root):
            pass
            #print(f"Root Console: {event.width}, {event.height}")
 
        

    def monitorcontrol(self, xi):
        """
        #Multiple Monitor Support Controls
        -----------------------------------
        #Finds which monitor is bigger and returns its index
        # index is the index
        # l holds the monitor sizes
        """
        
        monitors = []
        for x in get_monitors(): monitors.append([x.width, x.height])
        y = list(enumerate(monitors))
        l = []

        for z in y: l.append(sum(z[1]))
        if(xi == 'i'):
            m = min(l)
        elif(xi == 'x'):
            m = max(l)

        index = None
        for c, g in enumerate(l): 
            if g == m: index = c
        return l[index]
        
    def giveroot(self):
        return self.root

    def title(self, title="Turko App"):
        """
        Set the title of this app
        ---------------------------------
        E.g. turko.title("My App Name")
        """
        self.root.title(title)

    def minsize(self, minwidth=500, minheight=500):
        """
        Set the minimum size of this app's window
        ---------------------------------
        E.g. turko.minsize(500, 500)
        """
        self.root.minsize(minwidth, minheight)

    def maxsize(self, maxwidth=500, maxheight=500):
        """
        Set the maximum size of this app's window
        ---------------------------------
        We highly advise against setting a maxsize as your app should be resizable to any size for maximum user-friendliness
        E.g. turko.maxsize(500, 500)
        """
        self.root.maxsize(maxwidth, maxheight)
    def minmaxsize(self, minwidth=400, minheight=300, maxwidth=960, maxheight=780):
        """
        Set the minimum and maximum sizes of this app's window
        ---------------------------------
        E.g. turko.minmaxsize(300, 400, 1920, 1080)
        """
        self.root.minsize(minwidth, minheight)
        self.root.maxsize(maxwidth, maxheight)
    
    def __str__(self):
        return "root"
        
    def run(self):
        """
        Begin running Turko App
        ---------------------------------
        E.g. turko.mainloop()
        """
        self.root.mainloop()

    