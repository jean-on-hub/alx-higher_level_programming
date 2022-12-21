#!/usr/bin/python3
"""Define a Square class"""

class Square:
    """A square class"""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square
        
        Args:
        size (int): The size of the square
        position (tuple): The position of the square
        """
        self.__size = size
        self.__position = position
        
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
        
    @property
    def position(self):
        """Get the position of the square"""
        return self.__position
    
    @position.setter  
    def position(self, value):
        """Set the position of the square"""
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value
        
    def my_print(self):
        """Print the square with # character"""
        if self.__size == 0:
            print("")
            return 
        
        [print("") for i in range(0, self.__position[1])]
        for i in range(self.__size):
            [print(" ", end="") for k in range(0, self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print("")
        
