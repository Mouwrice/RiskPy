from board import Board
from abc import ABC


class Player(ABC):
    def __init__(self, name: str, player_id: int):
        self.name = name
        self.armies = 0
        self.id = player_id

    def claim_territory(self, board: Board):
        pass
