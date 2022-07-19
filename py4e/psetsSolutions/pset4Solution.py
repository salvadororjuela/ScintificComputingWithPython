class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.heigth = height

    def set_width(self, width):
        self.width = width
        return width

    def set_height(self, height):
        self.heigth = height
        return height

    def get_area(self):
        return self.width * self.heigth

    def get_perimeter(self):
        return (2 * self.width) + (2 * self.heigth)

    def get_diagonal(self):
        return ((self.width ** 2 + self.heigth ** 2) ** .5)

    def get_picture(self):
        picture = ""
        for i in range(self.width):
            for j in range(self.heigth):
                picture += ("*")
            picture += ("\n")
        return picture

    def get_amount_inside(self):
        pass

class Square(Rectangle):
        pass

rect = Rectangle(10, 5)
print(f"Width: {rect.width}")
print(f"Height: {rect.heigth}")
print(f"Area: {rect.get_area()}")
print(f"Perimeter: {rect.get_perimeter()}")
print(f"Diagonal: {rect.get_diagonal()}")
print(rect.get_picture())