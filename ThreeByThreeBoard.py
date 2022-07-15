import numpy as np
from IBoard import IBoard


class ThreeByThreeBoard(IBoard):
    def __init__(self):
        self.move_count = 0
        self._board_size = 3
        self._board = np.ndarray(
            shape=(self._board_size, self._board_size), dtype=int)
        self._board.fill(0)

    def _get_states(self, points: list[tuple[int, int]]) -> list[int]:
        result = []
        for pair in points:
            y = pair[0]
            x = pair[1]
            result += [self._board[x, y]]
        return result

    def check_victory(self) -> int:
        victory_combos = np.array([[(0, 0), (0, 1), (0, 2)],
                                   [(1, 0), (1, 1), (1, 2)],
                                   [(2, 0), (2, 1), (2, 2)],

                                   [(0, 0), (1, 0), (2, 0)],
                                   [(0, 1), (1, 1), (2, 1)],
                                   [(0, 2), (1, 2), (2, 2)],

                                   [(0, 0), (1, 1), (2, 2)],
                                   [(2, 2), (1, 1), (0, 0)]])
        results = [self._get_states(x) for x in victory_combos]
        if [1, 1, 1] in results:
            return 1
        elif [2, 2, 2] in results:
            return 2
        else:
            return 0

    def make_move(self, point: tuple[int, int], player: int) -> bool:
        y = point[0]
        x = point[1]
        if self._board[x, y] == 0:
            self._board[x, y] = player
            self.move_count += 1
            return True
        else:
            return False

    def get_board(self) -> np.array:
        return self._board
