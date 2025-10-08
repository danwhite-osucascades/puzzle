from enum import Enum

class Pos(Enum):
    LEFT = "left"
    RIGHT = "right"

    def toggle(self):
        return Pos.RIGHT if self is Pos.LEFT else Pos.LEFT