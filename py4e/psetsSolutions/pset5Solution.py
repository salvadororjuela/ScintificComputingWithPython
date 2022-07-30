import copy
import random
from re import findall

class Hat:
    # **kwargs is used to accept a variable number of arguments and represent them in a dictionary
    def __init__(self, **kwargs):
        self.contents = list()
        
        """convert self.copyKwargs into a list of strings that contains the colors times the number 
        of balls of the same color.
        i.e. {blue=4, red=2, green=3} into [blue, blue, blue, blue, red, red, green, green, green]"""
        for key, value in kwargs.items():
            # Append the color times the number.
            self.contents += [key] * value

    def draw(self, qtyDraw):
        drawnBalls = list()
        ball = ""
        length = len(self.contents)

        if qtyDraw >= length:
            return self.contents
        # Remove randomly the number of balls passed in to the method in the qtyDraw attribute
        # Generate random numbers the number of times passed in
        for i in range(qtyDraw):
            # Every number generated will remove the ball in the position corresponding to the random number
            # from self.contents and store it in the variable drawnBalls.
            ball = random.randint(0, length - 1) # Randon number. Length resembles a position, it can't have the same amount of the length or it will be out of range, that's why 1 is subtract from length
            
            # Append and remove to drawnBalls the element correspondig to the position ball (Random number)
            drawnBalls.append(self.contents.pop(ball))

            # It is necessary to subtract 1 to len(self.contets) - 1 to avoid an error because the new generated number could be out of range
            length -= 1

        return drawnBalls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    matches = 0

    # Execute the experiment the num_experimets indicated
    for i in range(num_experiments):
        # If match remains true it will add 1 to matches
        match = True
        #
        drawElementsDict = dict()
        # deepcopy() required for prescision
        repeatedElements = copy.deepcopy(hat)
        # Use the experimentDrawnBalls method from the Hat class to get the random balls with the number of balls to draw
        experimentDrawnBalls = repeatedElements.draw(num_balls_drawn)
        
        # Iterates over the drawn balls list of strings returned by the draw method: ["blue", "red", "blue"] and turns the 
        # values into a dictionary: {"blue": 2, "red":1}
        for element in experimentDrawnBalls:
            # Add 1 to each element in the dictionary until the key value pairs are completed
            values = drawElementsDict.get(element, 0)
            drawElementsDict[element] = values + 1

        # Validate if the minimum matches are reached comparing expected balls against the drawn balls
        for element, values in expected_balls.items():
            # If the values don't match, the loop breaks
            if drawElementsDict.get(element, 0) < values:
                match = False
                break
        
        # If match remains True add 1 to the matches counter.
        if match == True:
            matches += 1

    # Probability of getting the expected balls in n num_experiments
    return matches/num_experiments


hat = Hat(blue=3,red=2,green=6)
# print(hat.contents)
# print(hat.draw(3))
print(experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000))