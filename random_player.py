from player import Player
from board import Board
import random


class RandomPlayer(Player):

    def claim_territory(self, board: Board):
        territory = random.randint(0, len(board.free_territories) - 1)
        board.claim_territory(territory, self)

    def place_armies(self, board: Board):
        """
        Place armies on 1 territory
        :return: Empty list if the player does not want to place armies
        else [(armies, territory)]
        """
        army_placement = []
        territories = list(self.territories)
        amount = random.randint(0, len(territories) - 1)
        armies_placed = 0
        for _ in range(amount):
            if self.armies - armies_placed == 0:
                return army_placement

            index = random.randint(0, len(territories) - 1)
            armies = random.randint(1, self.armies - armies_placed)

            army_placement.append((armies, territories[index]))
            del territories[index]
            armies_placed += armies

        return army_placement

    def attack(self, board: Board):
        pass
