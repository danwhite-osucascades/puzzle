from piece import Piece
from robot import Robot
from position import Pos
from puzzle_error import PuzzleError

class Game:
    def __init__(self):
        self.pieces = {
            "A": Piece("A"),
            "B": Piece("B"),
            "C": Piece("C")
        }

        self.robot = Robot()

    def move(self):
        self.robot.move()
        if self.check_state():
            print("Congratulations! You win!")

    def grab(self, piece):
        self.robot.grab(self.pieces[piece])

    def release(self):
        self.robot.release()

    def check_state(self):
        if self.pieces['A'].position == Pos.RIGHT and self.pieces['B'].position == Pos.RIGHT and self.pieces['C'].position == Pos.RIGHT:
            return True
        else:
            if self.robot.position != self.pieces['B'].position:
                if self.pieces['B'].position == self.pieces['A'].position:
                    raise PuzzleError(f"Piece B and Piece A are both on the {self.pieces['B'].position} side, and the robot is on the {self.robot.position} side.")
                elif self.pieces['B'].position == self.pieces['C'].position:
                    raise PuzzleError(f"Piece B and Piece C are both on the {self.pieces['B'].position} side, and the robot is on the {self.robot.position} side.")
                else:
                    return False