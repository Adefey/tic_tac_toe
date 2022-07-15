from abc import ABC
from enum import Enum
import numpy as np

class IBoard(ABC):

    def check_victory(self) -> int:
        pass

    def make_move(self, point: tuple[int, int], player: int) -> bool:
        pass

    def get_board(self) -> np.array:
        pass
