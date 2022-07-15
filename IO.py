import numpy as np
from IBoard import IBoard
from IPlayer import IPlayer


def print_board(board: np.array):
    for i in range(0, board.shape[0]):
        for j in range(0, board.shape[1]):
            if board[i, j] == 1:
                print('X\t', end='')
            elif board[i, j] == 2:
                print('O\t', end='')
            else:
                print(' \t', end='')
        print('')


def print_victory_message(player: IPlayer):
    print(f'{player.name} wins')
