#!/usr/bin/python3
"""Empty class Square that defines a square"""


class Square:
    """Empty class Square that defines a square"""
    def __init__(self, size):
        self.__size = size
    def get_size(self):
        return self.__size
    def set_size(self, size):
        self.__size = size
    """pass"""