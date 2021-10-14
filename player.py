from board import Board
from abc import ABC
from territory import Territory


class Player(ABC):
    def __init__(self, name: str, color: str):
        self.name = name
        self.armies = 0
        self.id = None
        self.color = color
        self.territories: set = set()
        self.continents: set = set()

    def claim_territory(self, board: Board):
        pass

    def place_armies(self, board: Board):
        """
        Place armies on 1 territory
        :return: Empty list if the player does not want to place armies
        else [(armies, territory)]
        """
        pass

    def attack(self, board: Board):
        pass

    def defend(self, dice: int, attacker: Territory, defender: Territory, board: Board):
        pass

    def free_move(self, board: Board):
        pass

    def colorize_text(self, text: str):
        return f'{self.color}{text}\033[00m'
