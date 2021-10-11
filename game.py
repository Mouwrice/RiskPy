from board import Board
from player import Player
import dice


class Game:
    def __init__(self, players: [Player], board: Board):
        self.players = players
        self.board = board
        self._first_player = 0

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
        print(f"Highest roller gets to place it's armies first!\n")
        rolls = dice.players_roll_dice(self.players)
        players = [i for i in range(len(self.players))]
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
                    rolls = dice.players_roll_dice([self.players[player] for player in players])

        self._first_player = players[0]
        print(f"{self.players[self._first_player].name.capitalize()} may begin!")

        player = self._first_player
        while self.board.free_territories:
            self.players[player].claim_territory(self.board)

        print(self.board)

