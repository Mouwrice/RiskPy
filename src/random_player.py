from player import Player
from board import Board
import random
from territory import Territory


class RandomPlayer(Player):

    def claim_territory(self, board: Board):
        return random.randint(0, len(board.free_territories) - 1)

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

    def attack(self, board: Board, attack_chance: float = 0.5):
        # Chance to attack
        if random.random() >= attack_chance:
            return None

        # Create valid attacks, chooses a random connection to an enemy territory
        valid_attacks = []
        for territory in self.territories:
            # A territory should have at least 2 armies
            if territory.armies >= 2:
                # Can only attack from a territory adjacent to an enemy territory
                enemy_territories = []
                for enemy_territory in territory.connections:
                    if enemy_territory.player != self:
                        enemy_territories.append(enemy_territory)
                if len(enemy_territories) > 0:
                    valid_attacks.append((territory, random.choice(enemy_territories)))

        if len(valid_attacks) == 0:
            return None

        (attacker, defender) = valid_attacks[random.randint(0, len(valid_attacks) - 1)]
        dice = random.randint(1, min(attacker.armies - 1, 3))  # Attacker may only use a maximum of 3 dices
        return dice, attacker, defender

    def capture(self, dice: int, attacker: Territory, defender: Territory):
        return random.randint(dice, attacker.armies - 1)

    def defend(self, dice: int, attacker: Territory, defender: Territory, board: Board):
        return min(2, defender.armies)

    def free_move(self, board: Board):

        valid_origins = []
        for territory in self.territories:
            if territory.armies > 1:
                valid_origins.append(territory)

        if not valid_origins:
            return

        origin = random.choice(valid_origins)

        valid_destinations = []
        for territory in origin.connections:
            if territory.player == self:
                valid_destinations.append(territory)

        if not valid_destinations:
            return None

        destination = random.choice(valid_destinations)
        armies = random.randint(1, origin.armies - 1)
        return armies, origin, destination


class RandomPeacefulPlayer(RandomPlayer):
    """
    Never attacks
    """
    def attack(self, board: Board, attack_chance=0):
        return None


class RandomHostilePlayer(RandomPlayer):
    """
    Always attacks and always places armies
    """
    def attack(self, board: Board, attack_chance=1):
        return super().attack(board, attack_chance)
