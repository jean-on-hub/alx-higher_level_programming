#!/usr/bin/python3
"""Define a Square class"""

class Square:
    """A square class"""

    def __init__(self, size=0):
        """Initialize a new square

        Args:
        size (int): The size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
