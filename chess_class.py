class Chess:
    '''
        A Chess class with all the possible moves. Decide the initial position and 
        provide the steps. All the moves are defined as methods which return True/False
        based on whether the move is possible or not. The class is currently configured
        for 8X8 chess board but it is scalable merely by chaning the value of 
        MAX_ROW_COLUMN class variable. Define separate classes or functions for 
        various chess characters and utilize the moves from this class.     
    '''
    MAX_ROW_COLUMN = 8 # Because square board is always a square matrix
    MIN_ROW_COLUMN = 0

    def __init__(self, row=1, column=1):
        self.row = row
        self.column = column
    
    def go_right(self, steps):

        if (self.column + steps) < Chess.MAX_ROW_COLUMN:
            self.column += steps
            return True
        else:
            return False

    def go_left(self, steps):

        if (self.column - steps) > Chess.MIN_ROW_COLUMN:
            self.column -= steps
            return True
        else:
            return False

    def go_up(self, steps):
        if (self.row - steps) > Chess.MIN_ROW_COLUMN:
            self.row -= steps
            return True
        else:
            return False

    def go_down(self, steps):
        if (self.row + steps) < Chess.MAX_ROW_COLUMN:
            self.row += steps
            return True
        else:
            return False

    def go_diag_right_down(self, steps):
 
        if (self.go_right(steps)) and (self.go_down(steps)):
            return True
        else:
            return False

    def go_diag_right_up(self, steps):

        if (self.go_right(steps)) and (self.go_up(steps)):
            return True
        else:
            return False

    def go_diag_left_down(self, steps):

        if (self.go_left(steps)) and (self.go_down(steps)):
            return True
        else:
            return False

   def go_diag_left_up(self, steps):

        if (self.go_left(steps)) and (self.go_up(steps)):
            return True
        else:
            return False

    def go_knight(self, direction):
        '''
            pass a tuple of directions to move. 
            e.g. ('L','D') --> left,down
        '''
