import numpy as np
from IBoard import IBoard


class ThreeByThreeBoard(IBoard):
    def __init__(self):
        self.move_count = 0
        self._board_size = 3
        self._board = np.ndarray(
            shape=(self._board_size, self._board_size), dtype=int)
        self._board.fill(0)

    def check_victory(self) -> int:
        # По строкам
        for i in range(0, self._board_size-1):
            beaten_cross: int = 0
            beaten_zero: int = 0
            for j in range(0, self._board_size-1):
                if self._board[i, j] == 1:
                    beaten_cross += 1
                elif self._board[i, j] == 2:
                    beaten_zero += 1
                if beaten_cross == self._board_size:
                    return 1
                elif beaten_zero == self._board_size:
                    return 2

        # По столбцам
        for j in range(0, self._board_size-1):
            beaten_cross: int = 0
            beaten_zero: int = 0
            for i in range(0, self._board_size-1):
                if self._board[i, j] == 1:
                    beaten_cross += 1
                elif self._board[i, j] == 2:
                    beaten_zero += 1
                if beaten_cross == self._board_size:
                    return 1
                elif beaten_zero == self._board_size:
                    return 2

        # По диагоналям
        for i in range(0, self._board_size-1):
            beaten_cross: int = 0
            beaten_zero: int = 0
            if self._board[i, i] == 1:
                beaten_cross += 1
            elif self._board[i, i] == 2:
                beaten_zero += 1
            if beaten_cross == self._board_size:
                return 1
            elif beaten_zero == self._board_size:
                return 2
        for i in range(self._board_size-1, 0, -1):
            beaten_cross: int = 0
            beaten_zero: int = 0
            if self._board[i, i] == 1:
                beaten_cross += 1
            elif self._board[i, i] == 2:
                beaten_zero += 1
            if beaten_cross == self._board_size:
                return 1
            elif beaten_zero == self._board_size:
                return 2

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
