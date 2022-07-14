from IPlayer import IPlayer


class HumanPlayer(IPlayer):

    def enter_cell(self) -> tuple[int, int]:
        x: int = input('Enter x coordinate: ')
        y: int = input('Enter y coordinate: ')
        return (x, y)
