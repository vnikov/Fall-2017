#
# ps10pr4.py  (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps10pr3 import *

class AIPlayer(Player):
    """ An intelligent player"""

    def __init__(self, checker, tiebreak, lookahead):
        """ a constructor for AIPlayer """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """ returns a string representing an AIPlayer object """
        return super().__repr__() + " (" + self.tiebreak + ", " + str(self.lookahead) + ")"

    def max_score_column(self, scores):
        """ takes a list scores containing a score for each column of the
        board, and that returns the index of the column with the maximum
        score """
        col_indices = []
        for i in range(len(scores)):
            if scores[i] == max(scores):
                col_indices += [i]
        if len(col_indices) == 1 or self.tiebreak == 'LEFT':
            return col_indices[0]
        elif self.tiebreak == 'RIGHT':
            return col_indices[-1]
        else:
            return random.choice(col_indices)

    def scores_for(self, board):
        """ determines the called AIPlayer‘s scores for the columns in board """
        scores = [0] * board.width
        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:
                if not board.can_add_to(col):
                    scores[col] = -1
                board.add_checker(self.checker, col)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(board)
                opp_move = opp.max_score_column(opp_scores)
                if board.is_win_for(self.checker) or opp_scores[opp_move] == 0:
                    scores[col] = 100
                elif 100 in opp_scores:
                    scores[col] = 0
                else:
                    scores[col] = 50
                board.remove_checker(col)
        return scores

    def next_move(self, board):
        """ return the called AIPlayer‘s judgment of its best possible
        move """
        self.num_moves += 1
        return self.max_score_column(self.scores_for(board))
