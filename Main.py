from HumanPlayer import HumanPlayer
from ThreeByThreeBoard import ThreeByThreeBoard
from IO import *
import os


def main():
    board = ThreeByThreeBoard()
    players = [HumanPlayer('Alice'), HumanPlayer('Bob')]
    while (board.check_victory() == 0) or (board.move_count < 9):
        print_board(board.get_board())
        print(f"Player {players[0].name}'s move")
        while not board.make_move(players[0].enter_cell(), 1):
            continue
        print_board(board.get_board())
        print(f"Player {players[1].name}'s move")
        while not board.make_move(players[1].enter_cell(), 2):
            continue
        os.system('clear')
    print_victory_message(board.check_victory())


if __name__ == '__main__':
    main()
