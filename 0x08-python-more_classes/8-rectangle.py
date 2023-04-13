#!/usr/bin/python3
"""docsting for Rectangle"""


class Rectangle:
    """number of instances"""
    number_of_instances = 0
    """set print symbol character"""
    print_symbol = "#"
    """doctring for init"""
    def __init__(self, width, height):
        Rectangle.number_of_instances += 1
        self.height = height
        self.width = width
    """width getter method"""
    @property
    def width(self):
        return self.__width
    """height getter method"""
    @property
    def height(self):
        return self.__height
    """width getter method"""
    @width.setter
    def width(self, value):
        if isinstance(value, int) and value >= 0:
            self.__width = value
        elif not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
    """height getter method"""
    @height.setter
    def height(self, value):
        if isinstance(value, int) and value >= 0:
            self.__height = value
        elif not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
    """calculate the area of rectangle"""
    def area(self):
        return (self.width * self.height)
    """calculate the perimeter of rectangle"""
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (2 * (self.width + self.height))
    """print rectangle"""
    def __str__(self):
        string = ''
        if self.width == 0 or self.height == 0:
            return str()
        for i in range(self.height):
            if i != 0:
                string += '\n'
            for j in range(self.width):
                """**Note to self**
                Use instance attribute/method to change for the instance
                and not the class.
                The class attribute/method affects all instances"""
                string += str(self.print_symbol)
        return string
    """string representation"""
    def __repr__(self):
        string = f'Rectangle({self.width}, {self.height})'
        return string
    """delete object"""
    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
    """returns the biggest rectangle based on the area"""
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        elif rect_1.area() == rect_2.area():
            return rect_2 
