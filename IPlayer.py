from abc import ABC


class IPlayer(ABC):

    def __init__(self, new_name: str):
        self.name = new_name

    def enter_cell(self) -> tuple[int, int]:
        pass
