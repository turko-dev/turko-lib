import tkinter as tk

class Frame:
    def __init__(self, core, padding=0):
        pass


class Button:
    def __init__(self, parent, text="Button", command=None, **kwargs):
        self.button = tk.Button(parent, text=text, command=command, **kwargs)
        self.button.grid(column=1, row=0)
        
def calcWidth(screenWidth, percentage):
    percentage = str(percentage)
    if '%' in percentage:
        plist = []
        flist = ""
        for x in percentage: plist.append(x)
        plist.remove('%')
        for y in plist: flist += y
        try:
            f = int(flist)
            print(f)
            print(type(f))
        except Exception:
            print("Error")

        p = f / 100
        print(p)
        print(screenWidth)
        print(f"{screenWidth * p}")
        return screenWidth * p
    #p = percentage / 100
    #print(f"{screenWidth * p}")
