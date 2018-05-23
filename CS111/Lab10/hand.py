#
# hand.py
#
# CS 111, Boston University
#

from card import *

class Hand:
    """ a class for objects that represent a single hand of cards """

    def __init__(self):
        """ constructor for Hand objects """
        self.cards = []

    def __repr__(self):
        """ returns a string representation of the called Hand object (self) """
        return str(self.cards)

    def add_card(self, card):
        """ add the specified Card object (card) to the list of cards
            for the called Hand object (self)
        """
        self.cards += [card]

    def num_cards(self):
        """ returns the number of cards in the called Hand object (self) """
        return len(self.cards)

    def get_value(self):
        """ returns the total value of the cards in the called Hand object (self) """
        value = 0
        for card in self.cards:
            value += card.get_value()
        return value

    def has_any(self, rank):
        """ returns True if there is at least one occurrence of a Card with
        that rank in the called Hand object (self), and that returns False if
        there are no occurrences of that rank in the Hand """
        for card in self.cards:
            if card.rank == rank:
                return True
        return False

class BlackjackHand(Hand):
    """ a class for playing Blackjack """
    
    def get_value(self):
        """ return the sum of the value of all cards """
        value = super().get_value()
        if self.has_any('A') and value < 12:
            value += 10
        return value
