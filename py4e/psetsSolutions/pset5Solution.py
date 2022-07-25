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
        
        print(f"Initial contents: {self.contents}")
            
    def draw(self, qtyDraw):
        drawnBalls = list()
        ball = ""
        length = len(self.contents)
        # Check that the numbers of ball to draw is less or equal than the quantity of balls in self.contents
        if qtyDraw > len(self.contents):
            return False
        # Else remove randomly the number of balls passed in to the method in the qtyDraw attribute
        else:
            # Generate random numbers the number of times passed in
            for i in range(qtyDraw):
                # Every number generated will remove the ball in the position corresponding to the random number
                # from self.contents and store it in the variable drawnBalls.
                ball = random.randint(0, length - 1) # Randon number. Length resembles a position, it can't have the same amount of the length or it will be out of range, that's why 1 is subtract from length
                
                try:
                    drawnBalls.append(copy.copy(self.contents[ball])) # Append to drawnBalls the element correspondig to the position ball (Random number)
                except:
                    print(f"ERROR 'Balls out of range'")

                del self.contents[ball] # Delete the item from self.contents
                # It is necessary to subtract 1 to len(self.contets) - 1 to avoid an error because the new generated number could be out of range
                length -= 1
                
        return drawnBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    pass


hat = Hat(blue=4, red=2, green=6)
hat.draw(2)