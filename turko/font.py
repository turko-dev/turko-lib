from tkinter import font

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

