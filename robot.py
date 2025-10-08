from position import Pos
from piece import Piece
from puzzle_error import PuzzleError

class Robot:
    def __init__(self):
        self.position = Pos.LEFT
        self.holding = None

    def move(self):
        self.position = self.position.toggle()
        if self.holding:
            self.holding.position = self.holding.position.toggle()
    
    def grab(self, piece: Piece):
        if self.holding:
            raise PuzzleError(f"Robot can't pick up piece {piece.name} because it is already holding {self.holding.name}.")
        elif self.position != piece.position:
            raise PuzzleError(f"Robot can't pick up piece {piece.name} because the robot is on the {self.position} side and the pice is on the {piece.position} side.")
        else:
            self.holding = piece
            
    def release(self):
        if self.holding:
            self.holding = None
        else:
            raise PuzzleError(f"Robot has nothing to release.")