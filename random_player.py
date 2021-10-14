from player import Player
from board import Board
import random
from territory import Territory


class RandomPlayer(Player):

    def claim_territory(self, board: Board):
        territory = random.randint(0, len(board.free_territories) - 1)
        board.claim_territory(territory, self)

    def place_armies(self, board: Board):
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
        # Chance to attack
        if random.random() > 0.5:
            return None

        # Create valid attacks, chooses a random connection to an enemy territory
        valid_attacks = []
        for territory in self.territories:
            # A territory should have at least 2 armies
            if territory.armies >= 2:
                # Can only attack from a territory adjecent to an enemy territory
                enemy_territories = []
                for enemy_territory in territory.connections:
                    if enemy_territory.player != self:
                        enemy_territories.append(enemy_territory)
                if len(enemy_territories) > 0:
                    valid_attacks.append((territory, random.choice(enemy_territories)))

        if len(valid_attacks) == 0:
            return None

        (attacker, defender) = valid_attacks[random.randint(0, len(valid_attacks) - 1)]
        dice = random.randint(1, min(attacker.armies - 1, 3))  # Attacker may only use a maximum of 3 dice
        return dice, attacker, defender

    def defend(self, dice: int, attacker: Territory, defender: Territory, board: Board):
        return min(2, defender.armies)


class RandomPeacefulPlayer(RandomPlayer):
    def attack(self, board: Board):
        return None
