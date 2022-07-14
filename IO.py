import numpy as np
from IBoard import Players
from IBoard import IBoard
from IPlayer import IPlayer


def print_board(board: np.array):
    for i in range(0, board.shape[0]):
        for j in range(0, board.shape[1]):
            if board[i, j] == Players.Cross:
                print('X\t')
            elif board[i, j] == Players.Zero:
                print('O\t')
            elif board[i, j] == Players.NoOne:
                print(' \t')


def print_victory_message(player: IPlayer):
    print(f'{player.name} wins')
