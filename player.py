from board import Board
from abc import ABC


class Player(ABC):
    def __init__(self, name: str, player_id: int, color: str):
        self.name = name
        self.armies = 0
        self.id = player_id
        self.color = color

    def claim_territory(self, board: Board):
        pass

    def colorize_text(self, text: str):
        return f'{self.color}{text}\033[00m'
