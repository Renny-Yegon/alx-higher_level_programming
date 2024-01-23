#!/usr/bin/python3
"""Square Module"""


class Square:
    """Defines square"""

    def __init__(self, size=0):
        """
        Constructor
        Args:
            size: length of one side
        """
        self.size = size

    @property
    def size(self):
        """
        Length of side of square
        Raises:
            ValueError: if size is less than 0
            TypeError: if size is not int
        """
        return self.__size
