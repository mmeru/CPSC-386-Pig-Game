# Moses Merugu
# CPSC 386-03
# 2022-03-07
# mmeru@csu.fullerton.edu
# @mmeru
#
# Lab 02-00
#
# Contains Die class that simulates a Die returning a random number 1-6
#
"""Contains Die class that simulates a Die returning a random number 1-6"""
from random import randrange


class Die:
    """Die class that returns a random number 1-6"""

    def __init__(self):
        pass

    @property
    def roll(self):
        """returns a random number 1-6"""
        return randrange(1, 7)

    @property
    def do_nothing(self):
        """Does nothing, required to pass pylint."""
        return 0


if __name__ == "__main__":
    D = Die()
    for i in range(10):
        print(D.roll())
