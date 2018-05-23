class Board:
    """ A Connect Four class """
    def __init__(self, height, width):
        """ constructs a new Board object """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """ returns a string representing a Board object """
        s = ''
        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'
        s += ( '-' * self.width * 2 ) + '\n'
        for i in range(self.width):
            s += ' ' + str(i % 10)
        return s

    def add_checker(self, checker, col):
        """ add a checker into a board """
        row = 0
        while row < self.height - 1 and self.slots[row + 1][col] == ' ':
            row += 1
        self.slots[row][col] = checker

    def reset(self):
        """ reset the Board object """
        self = self.__init__(self.height, self.width)

    def add_checkers(self, columns):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'
        for col_str in columns:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """  returns True if it is valid to place a checker in the
        column col on the calling Board object. Otherwise, it should
        return False """
        if col in range(self.width):
            if self.slots[0][col] == ' ':
                return True
        return False

    def is_full(self):
        """ returns True if the called Board object is completely full
        of checkers, and returns False otherwise """
        full = True
        for col in range(self.width):
            if self.can_add_to(col):
                full = full and False
        return full

    def remove_checker(self, col):
        """ removes the top checker from column col of the called Board
        object """
        if self.slots[self.height - 1][col] != ' ':
            row = 0
            while self.slots[row][col] == ' ':
                row += 1
            self.slots[row][col] = ' '

    def is_win_for(self, checker):
        """ returns True if there are four consecutive slots containing
        checker on the board. Otherwise, it should return False """
        return self.is_horizontal_win(checker) or self.is_vertical_win(checker) or self.is_down_diagonal_win(checker) or self.is_up_diagonal_win(checker)

    def is_horizontal_win(self, checker):
        """ check if the checker wins horizontally or not """
        for row in range(self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and self.slots[row][col+1] == checker and self.slots[row][col+2] == checker and self.slots[row][col+3] == checker:
                    return True
        return False

    def is_vertical_win(self, checker):
        """ check if the checker wins vertically or not """
        for row in range(self.height - 3):
            for col in range(self.width):
                if self.slots[row][col] == checker and self.slots[row+1][col] == checker and self.slots[row+2][col] == checker and self.slots[row+3][col] == checker:
                    return True
        return False

    def is_down_diagonal_win(self, checker):
        """ check if the checker wins diagonally downward or not
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and self.slots[row+1][col+1] == checker and self.slots[row+2][col+2] == checker and self.slots[row+3][col+3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """ check if the cheker wins diagonally upward or not
        """
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                if self.slots[self.height - 1 - row][col] == checker and self.slots[self.height - 1 - row - 1][col+1] == checker and self.slots[self.height - 1 - row - 2][col+2] == checker and self.slots[self.height - 1 - row - 3][col+3] == checker:
                    return True
        return False
