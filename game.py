from board import Board
from player import Player
import dice
from territory import Territory


def first_player(players: [Player]):
    rolls = dice.players_roll_dice(players)
    players = [i for i in range(len(players))]
    highest = rolls[0]
    i = 1
    loop = 0
    while len(players) > 1:
        if rolls[i] < highest:
            players.pop(i)
            rolls.pop(i)
        else:
            highest = rolls[i]
            i += 1
        if 1 < len(players) == i:
            i = 0
            loop += 1
            if loop == 2:
                loop = 0
                rolls = dice.players_roll_dice([players[player] for player in players])

    return players[0]


class Game:
    def __init__(self, players: [Player], board: Board):
        self.players = players
        self.board = board
        self.game_over = False

    def setup(self):
        """
        Initial occupation of territories
        """
        print("--- SETUP ---\n")
        armies_per_players = [50, 35, 30, 25, 20][len(self.players) - 2]
        print(f'Armies per player: {armies_per_players}\n')

        # Every player receives initial amount of armies
        for player in self.players:
            player.armies = armies_per_players

        # Decide who gets to go first
        print("Highest roller gets to place it's armies first!\n")
        player = first_player(self.players)
        print(f"{self.players[player].name.capitalize()} may begin!\n")

        while self.board.free_territories:
            print(self.board)
            self.players[player].claim_territory(self.board)
            player = (player + 1) % 4

        print(self.board)

    def accumulate_armies(self, player: Player):
        pass

    def verify_attack(self, die: int, attacker: Territory, defender: Territory):
        pass

    def verify_defense(self, die: int, attacker: Territory, defender: Territory):
        pass

    def simulate_attack(self, die: int, attacker: Territory, defender: Territory):
        self.verify_attack(die, attacker, defender)
        pass

    def verify_free_move(self, armies: int, origin: Territory, destination: Territory):
        pass

    def execute_free_move(self, armies: int, origin: Territory, destination: Territory):
        self.verify_free_move(armies, origin, destination)

    def play(self):
        print("Highest roller gets to go first!\n")
        player = first_player(self.players)

        while not self.game_over:
            self.accumulate_armies(self.players[player])
            self.players[player].place_armies(self.board)

            attack = self.players[player].attack(self.board)
            while attack is not None:
                (die, attacker, defender) = attack
                self.simulate_attack(die, attacker, defender)
                attack = self.players[player].attack(self.board)

            free_move = self.players[player].free_move()
            if free_move is not None:
                (armies, origin, destination) = free_move
                self.execute_free_move(armies, origin, destination)

            player += 1
            player %= len(self.players)
