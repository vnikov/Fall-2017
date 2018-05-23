#
# ps10pr2.py  (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#  

from ps10pr1 import Board

# write your class below

class Player():

    def __init__(self, checker):
        """ A constructor of a Player class """
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """ returns a string representing a Player object """
        return 'Player ' + self.checker

    def opponent_checker(self):
        """ returns a one-character string representing the checker
        of the Player object’s opponent """
        if self.checker == 'O':
            return 'X'
        else:
            return 'O'

    def next_move(self, board):
        """ returns the column where the player wants to make the next
        move """
        while True:
            move = int(input("Enter a column:"))
            if move in range(board.width):
                self.num_moves += 1
                return move
            print("Try again!")
