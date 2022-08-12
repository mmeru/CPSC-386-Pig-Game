# Moses Merugu
# CPSC 386-03
# 2022-03-07
# mmeru@csu.fullerton.edu
# @mmeru
#
# Lab 02-00
#
# Contains Player and Computer Player class and their respective functions
#
"""Contains Player and Computer Player class and their respective functions"""


class Player:
    """Player class"""

    def __init__(self, name, order):
        self._name = name
        self._score = 0
        self._order = order

    @property
    def name(self):
        """Returns player name"""
        return self._name

    @property
    def order(self):
        """Returns player order"""
        return self._order

    @property
    def score(self):
        """Returns player score"""
        return self._score

    @score.setter
    def score(self, new_score):
        self._score = new_score

    @staticmethod
    def does_roll():
        """CPU player roll decision"""
        return True

    @staticmethod
    def am_i_human():
        """If player is human or CPU"""
        return True

    def __str__(self):
        return self._name

    def __repr__(self):
        return 'Player("{}", {})'.format(self._name, self._order)


class ComputerPlayer(Player):
    """Computer Player class"""

    def __init__(self, order, game):
        super().__init__("GlaDos", order)
        self._game = game

    def am_i_human(self):
        return False

    # def are_you_real(self):
    # return self._game.am_i_real()

    def does_roll(self):
        opponent_score = self._game.opponent_score(self)
        return bool(opponent_score > self._score)
