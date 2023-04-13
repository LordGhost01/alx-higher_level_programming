#!/usr/bin/python3
"""docsting for Rectangle"""


class Rectangle:
    """doctring for init"""
    def __init__(self, width, height):
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
                string += '#'
        return string 
