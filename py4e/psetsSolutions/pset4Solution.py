class Rectangle:
    # Define attributes
    def __init__(self, width=1, height=1):
        self.width = width
        self.heigth = height

    # Set the shape width
    def set_width(self, width):
        self.width = width
        return width

    # Set the shape height
    def set_height(self, height):
        self.heigth = height
        return height

    # Area
    def get_area(self):
        return self.width * self.heigth

    # Perimeter
    def get_perimeter(self):
        return (2 * self.width) + (2 * self.heigth)

    # Diagonal
    def get_diagonal(self):
        return ((self.width ** 2 + self.heigth ** 2) ** .5)

    # Print the shape using a nested loop
    def get_picture(self):
        picture = ""
        for i in range(self.heigth):
            for j in range(self.width):
                picture += ("*")
            picture += ("\n")
        return picture

    def get_amount_inside(self):
        pass
    
    # Return the string when the instance is represented
    def __str__(self):
        rectangleStr = f"{self.__class__.__qualname__}(width= {self.width}, height= {self.heigth})"
        squareStr = f"{self.__class__.__qualname__}(side= {self.width})"
        
        if self.__class__.__qualname__ == "Rectangle":
            return rectangleStr
        else:
            return squareStr

class Square(Rectangle):
    # Defines the width and height for a square with the same side length
    def __init__(self, width):
        self.set_side(width)
    
    # Define that the meassuremet is the same for height and width
    def set_side(self, width):
        # The super replaces the default value of the height variable in the superclass with
        # the value of the width
        self.width = width
        super(Square, self).__init__(width, height=width)


rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
# print(rect.get_amount_inside(sq))