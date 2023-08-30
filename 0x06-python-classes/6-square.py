#!/usr/bin/python3

"""Define a class Square"""


class Square:
    """Represent a Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Intialize a new Squre

        Args:
            size (int): the size of the new square must be >= 0
        """
        self.__position = position
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Return the area of the current Square instance"""
        return self.__size * self.__size

    def my_print(self):
        """Print the square to stdout"""
        if self.__size == 0:
            print()
        else:
            if self.__position[1] <= 0:
                for _ in range(self.__position[1]):
                    print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    @property
    def size(self):
        """Retrieve the size of the current Square instance"""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the current Square instance"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
