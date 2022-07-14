from abc import ABC
from enum import Enum
import numpy as np


class Players(Enum):
    Cross: int = 2
    Zero: int = 1
    NoOne: int = 0


class IBoard(ABC):
    def __init__(self):
        self.move_count : int = 0

    def check_victory(self) -> int:
        pass

    def make_move(self, point: tuple[int, int], player: int) -> bool:
        pass

    def get_board(self) -> np.array:
        pass
