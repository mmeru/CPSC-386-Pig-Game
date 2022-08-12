# Moses Merugu
# CPSC 386-03
# 2022-03-07
# mmeru@csu.fullerton.edu
# @mmeru
#
# Lab 02-00
#
# Contains PigGame class that contains pvp, pvc, and run functions
#
"""Contains PigGame class that contains pvp, pvc, and run functions"""
import time
from .dice import Die
from .player import Player, ComputerPlayer


class PigGame:
    """PigGame class"""

    def __init__(self):
        self._players = []

    def opponent_score(self, myself):
        """Returns opponent score"""
        for player in self._players:
            if myself != player:
                return player.score
        return None

    @staticmethod
    def pvp(c_p):
        """player vs player class"""
        roll_num = 0
        round_score = 0
        again = "y"
        dice = Die()

        while again == "y":
            roll = dice.roll
            roll_num = roll_num + 1
            print("\nRoll #{}".format(roll_num))
            if roll == 1:
                time.sleep(2)
                print("Ouch, {} rolled a 1.".format(c_p))
                round_score = 0
                again = "n"
            else:
                time.sleep(2)
                print("{} rolled a {}.".format(c_p, roll))
                round_score = round_score + roll
                print("{}, your ROUND score is {}".format(c_p, round_score))
                again = input("\n{}, roll again? (y/n) ".format(c_p))
        print("\n{}, your turn is over.".format(c_p))
        return round_score

    @staticmethod
    def pvc(c_p):
        """player vs cpu class"""
        roll_num = 0
        round_score = 0
        again = "y"
        dice = Die()
        while again == "y":
            roll = dice.roll
            roll_num = roll_num + 1
            print("\nRoll #{}".format(roll_num))
            if roll == 1:
                time.sleep(2)
                print("Ouch, {} rolled a 1.".format(c_p))
                round_score = 0
                again = "n"
            else:
                time.sleep(2)
                print("{} rolled a {}.".format(c_p, roll))
                round_score = round_score + roll
                print("{}, your ROUND score is {}\n".format(c_p, round_score))
                print("{}, roll again?".format(c_p))
                time.sleep(2)
                if c_p.does_roll() is True and round_score <= 12:
                    again = "y"
                    print("{} chose to roll.".format(c_p))
                else:
                    again = "n"
                    print("{} chose not to roll.".format(c_p))
                    time.sleep(2)
        print("\n{}, your turn is over.".format(c_p))
        return round_score

    def run(self):
        """Runs Pig Game"""
        dice = Die()
        num_players = int(input("How many players? [1-4] "))
        for _ in range(num_players):
            name = input("What is your name? ")
            order = dice.roll
            print("You rolled {}.".format(order))
            self._players.append(Player(name, order))
        if num_players == 1:
            order = dice.roll
            self._players.append(ComputerPlayer(order, self))
            print("{} rolled {}".format(self._players[1].name, order))

        print("\nBefore sorting ", self._players)
        self._players.sort(key=lambda p: p.order, reverse=True)
        print("After sorting ", self._players, "\n")

        c_p_i = 0

        if num_players == 1:
            while True:
                c_p = self._players[c_p_i]
                if c_p.am_i_human() is True:
                    print("{}, is up! TOTAL score: {}".format(c_p, c_p.score))
                    c_p.score = c_p.score + self.pvp(c_p)
                    print("{} has TOTAL score: {}\n".format(c_p, c_p.score))
                    time.sleep(2)
                else:
                    print("{}, is up! TOTAL score: {}".format(c_p, c_p.score))
                    c_p.score = c_p.score + self.pvc(c_p)
                    print("{} has TOTAL score: {}\n".format(c_p, c_p.score))
                    time.sleep(2)
                if c_p.score >= 30:
                    print(
                        "Congrats, {}! "
                        "You are the winner with a total score of {}!".format(
                            c_p, c_p.score
                        )
                    )
                    break
                c_p_i = (c_p_i + 1) % len(self._players)
        else:
            while True:
                c_p = self._players[c_p_i]
                print("{}, is up! TOTAL score: {}".format(c_p, c_p.score))
                c_p.score = c_p.score + self.pvp(c_p)
                print("{} has TOTAL score: {}\n".format(c_p, c_p.score))
                time.sleep(2)
                if c_p.score >= 30:
                    print(
                        "Congrats, {}! "
                        "You are the winner with a total score of {}!".format(
                            c_p, c_p.score
                        )
                    )
                    break
                c_p_i = (c_p_i + 1) % len(self._players)
