"""
This class holds the current Game State.

"""


class Moves:
    def __init__(self, start_square, end_square, board):
        self.start_row = start_square[0]
        self.start_col = start_square[1]
        self.end_row = start_square[0]
        self.end_col = end_square[1]
        self.moved_piece = board[self.start_row][self.start_col]
        self.end_location = board[self.end_row][self.end_col]


    def get_chess_notation(self):
