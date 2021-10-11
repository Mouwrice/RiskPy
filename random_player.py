from player import Player
from board import Board
import random


class RandomPlayer(Player):

    def claim_territory(self, board: Board):
        territory = random.randint(0, len(board.free_territories) - 1)
        board.claim_territory(territory, self)
