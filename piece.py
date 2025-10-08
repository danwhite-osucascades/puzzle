from position import Pos

class Piece:
    def __init__(self, name):
        self.name = name
        self.position = Pos.LEFT
        self.held = False