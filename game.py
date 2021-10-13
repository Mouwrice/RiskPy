from board import Board
from player import Player
import dice
from territory import Territory


def first_player(players: [Player]):
    rolls = dice.players_roll_dice(players)
    players_index = [i for i in range(len(players))]
    highest = rolls[0]
    i = 1
    loop = 0
    while len(players_index) > 1:
        if rolls[i] < highest:
            players_index.pop(i)
            rolls.pop(i)
        else:
            highest = rolls[i]
            i += 1
        if 1 < len(players_index) == i:
            i = 0
            loop += 1
            if loop == 2:
                loop = 0
                rolls = dice.players_roll_dice([players[player] for player in players_index])

    return players_index[0]


class Game:
    def __init__(self, players: [Player], board: Board):
        self.players: [Player] = players
        self.board: Board = board
        self.game_over = False
        for i, player in enumerate(players):
            player.index = i

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
        print("-- SETUP COMPLETE --\n")

    def accumulate_armies(self, player: Player):
        armies = min(3, len(player.territories) // 3)
        print(f'{player.name.capitalize()} receives {armies} armies.')
        for continent in player.continents:
            extra = self.board.armies_per_continent[continent]
            armies += extra
            print(f'{player.name.capitalize()} receives {extra} armies for occupying the entirety of {continent.name}!')

        player.armies += armies
        print(f'{player.name.capitalize()} has received a total of {armies} armies. {player.name.capitalize()} now has '
              f'{player.armies} armies.\n')

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
        print("Highest roller gets to go play first!\n")
        player = first_player(self.players)
        print(f"{self.players[player].name.capitalize()} may begin!\n")

        turn = 1
        current_player = self.players[player]
        # while not self.game_over:
        for _ in range(20):
            print(f'\nTURN {turn}:\n')
            turn += 1

            print("Army Accumulation:")
            self.accumulate_armies(current_player)

            print("Army Placement:")
            army_placement = current_player.place_armies(self.board)
            if len(army_placement) == 0:
                print("No armies placed.")
            else:
                print(f'{current_player.name.capitalize()} places armies on:')
            for (armies, territory) in army_placement:
                print(f'    {territory.name}: {armies}')
                self.board.place_armies(territory, current_player, armies)

            print()
            print(self.board)
            print()

            attack = current_player.attack(self.board)
            while attack is not None:
                (die, attacker, defender) = attack
                self.simulate_attack(die, attacker, defender)
                attack = current_player.attack(self.board)

            free_move = current_player.free_move(self.board)
            if free_move is not None:
                (armies, origin, destination) = free_move
                self.execute_free_move(armies, origin, destination)

            player += 1
            player %= len(self.players)
            current_player = self.players[player]
