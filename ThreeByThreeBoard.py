import numpy as np
from IBoard import Players
from IBoard import IBoard


class ThreeByThreeBoard(IBoard):
    def __init__(self):
        self._board_size: int = 3
        self._board = np.ndarray(shape=(_board_size, _board_size), dtype=int).fill(0)

    def check_victory(self) -> int:
        # По строкам
        for i in range(0, _board_size-1):
            beaten_cross: int = 0
            beaten_zero: int = 0
            for j in range(0, _board_size-1):
                if _board[i, j] == Players.Cross:
                    beaten_cross += 1
                elif _board[i, j] == Players.Zero:
                    beaten_zero += 1
                if beaten_cross == _board_size:
                    return Player.Cross
                elif beaten_zero == _board_size:
                    return Player.Zero

        # По столбцам
        for j in range(0, _board_size-1):
            beaten_cross: int = 0
            beaten_zero: int = 0
            for i in range(0, _board_size-1):
                if _board[i, j] == Players.Cross:
                    beaten_cross += 1
                elif _board[i, j] == Players.Zero:
                    beaten_zero += 1
                if beaten_cross == _board_size:
                    return Player.Cross
                elif beaten_zero == _board_size:
                    return Player.Zero

        # По диагоналям
        for i in range(0, _board_size-1):
            beaten_cross: int = 0
            beaten_zero: int = 0
            if _board[i, i] == Players.Cross:
                beaten_cross += 1
            elif _board[i, i] == Players.Zero:
                beaten_zero += 1
            if beaten_cross == _board_size:
                return Player.Cross
            elif beaten_zero == _board_size:
                return Player.Zero
        for i in range(_board_size-1, 0, -1):
            beaten_cross: int = 0
            beaten_zero: int = 0
            if _board[i, i] == Players.Cross:
                beaten_cross += 1
            elif _board[i, i] == Players.Zero:
                beaten_zero += 1
            if beaten_cross == _board_size:
                return Player.Cross
            elif beaten_zero == _board_size:
                return Player.Zero

        return Player.NoOne

    def make_move(self, point: tuple[int, int], player: int) -> bool:
        if _board[point[0], point[1]] == Player.NoOne:
            _board[point[0], point[1]] = player
            move_count += 1
            return True
        else:
            return False

    def get_board(self) -> np.array:
        return _board
