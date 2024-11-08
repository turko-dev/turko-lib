import tkinter as tk
from tkinter import ttk

class Frame(tk.Tk):
    def __init__(self, core, width, height, padding=0):
        frame = ttk.Frame(core.core, width=width, height=height, padding=padding)
        frame.config(width=width, height=height)
        frame.grid()




            


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
