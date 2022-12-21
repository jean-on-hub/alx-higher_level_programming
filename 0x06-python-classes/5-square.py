#!/usr/bin/python3
"""Define a Square class"""

class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initialize a new square
        Args:
        size (int): The size of the square
        """
        self.__size = size
        
    def area(self):
        """Return the area of the square"""
        return self.__size ** 2
    
    @property
    def size(self):
        """Get the size of the square"""
        return self.__size
    
    @size.setter  
    def size(self, value):
        """Set the size of the square"""
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
        
    def my_print(self):
        """Print the square with # character"""
        for i in range(self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
