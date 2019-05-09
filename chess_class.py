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
            return True
        else:
            return False

    def go_left(self, steps):

        if (self.column - steps) > Chess.MIN_ROW_COLUMN:
            return True
        else:
            return False

    def go_up(self, steps):
        if (self.row - steps) > Chess.MIN_ROW_COLUMN:
            return True
        else:
            return False

    def go_down(self, steps):
        if (self.row + steps) < Chess.MAX_ROW_COLUMN:
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
            argument 0 can be L,R,U,D
            argument 1 can also be L,R,U,D
            together they make combinations 
        '''
        arg1_flag = False
        arg2_flag = False

        if direction[0] == 'L':
            arg1_flag = self.go_left(2)
        elif direction[0] == 'R':
            arg1_flag = self.go_right(2)
        elif direction[0] == 'U':
            arg1_flag = self.go_up(2)
        elif direction[0] == 'D':
            arg1_flag = self.go_down(2) 

        if direction[1] == 'L':
            arg2_flag = self.go_left(1)
        elif direction[1] == 'R':
            arg2_flag = self.go_right(1)
        elif direction[1] == 'U':
            arg2_flag = self.go_up(1)
        elif direction[1] == 'D':
            arg2_flag = self.go_down(1)

        if arg1_flag and arg2_flag:
            return True

        return False

if __name__ == "__main__":
    #Test case --> find all the possible moves for a king based on its position. 
    import time 
    print("start time: ", time.time())
    king = Chess(2,1)
    possible_moves = 0

    if king.go_left(1):
        possible_moves += 1

    if king.go_right(1):
        possible_moves += 1

    if king.go_up(1):
        possible_moves += 1

    if king.go_down(1):
        possible_moves += 1

    if king.go_diag_left_down(1):
        possible_moves += 1

    if king.go_diag_left_up(1):
        possible_moves += 1
    
    if king.go_diag_right_down(1):
        possible_moves += 1
    
    if king.go_diag_right_up(1):
        possible_moves += 1     
    
    print("Possible moves: ", possible_moves)

    print("end time: ", time.time())
