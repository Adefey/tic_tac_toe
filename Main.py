from HumanPlayer import HumanPlayer
from ThreeByThreeBoard import ThreeByThreeBoard
from IBoard import Players
from IO import *


def main():
    board = ThreeByThreeBoard()
    players = [HumanPlayer('Alice'), HumanPlayer('Bob')]
    while (board.check_victory() != Players.NoOne) and (board.move_count < 9):
        print_board(board.get_board())
        while not board.make_move(players[0].enter_cell()):
            continue
        print_board(board.get_board())
        while not board.make_move(players[1].enter_cell()):
            continue
        print_board(board.get_board())
    print_victory_message(board.check_victory())


if __name__ == '__main__':
    main()
