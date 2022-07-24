import copy
import random
from re import findall
# Consider using the modules imported above.

class Hat:
    # **kwargs is used to accept a variable number of arguments and represent them in a dictionary
    def __init__(self, **kwargs):
        self.initialContents = list()
        self.secondaryContents = list()
        self.contents = list()
        self.kwargs = kwargs
        
        """convert self.copyKwargs into a list of strings that contains the colors times the number 
        of balls of the same color.
        i.e. {blue=4, red=2, green=3} into [blue, blue, blue, blue, red, red, green, green, green]"""
        for key, value in self.kwargs.items():
            # Append the color times the number. Result: ['blueblueblue', 'redred', 'greengreengreengreengreengreen']
            self.initialContents.append(key * value)

        # It is necessary to read each of the keys in self.kwargs for later use as a regular expresion
        # in the inner loop to split each element of the self.initialContents and get the following result:
        # [['blue', 'blue', 'blue', 'blue'], [], [], [], ['red', 'red'], [], [], [], ['green', 'green', 'green', 'green', 'green', 'green']]
        for i in self.kwargs:
            for k in self.initialContents:
                string = findall(i, k)
                self.secondaryContents.append(string)
        
        # Append to the self.contents list only the non empty sub elements in self.secondaryContents.
        # Result: ['blue', 'blue', 'blue', 'blue', 'red', 'red', 'green', 'green', 'green', 'green', 'green', 'green']
        for i in self.secondaryContents:
            for k in i:
                if k != None:
                    self.contents.append(k)
        
        print(self.contents)
            
    def draw(self):
        pass
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat = Hat(blue=4, red=2, green=6)