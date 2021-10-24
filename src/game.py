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


def verify_attack(player: Player, die: int, attacker: Territory, defender: Territory):
    assert attacker.player == player, f'Invalid attack territory. Territory {attacker.name} should be owned by' \
                                      f'{player.name.capitalize()}'
    assert 0 < die < attacker.armies, f'Number of dies should be between 1 and 3 and one less than the amount of armies' \
                                      f'on the territory.\n' \
                                      f'armies: {attacker.armies}\n' \
                                      f'die:    {die}\n'
    assert defender.player != player, f'Can only attack other players, not yourself.'


def verify_defense(die: int, defender: Territory):
    assert 0 < die <= max(2, defender.armies), f'Incorrect number of dies used by the defender.\n' \
                                               f'{str(defender)}' \
                                               f'die: {die}'


def verify_free_move(armies: int, origin: Territory, destination: Territory, player: Player):
    assert origin.player == player, f"Can only move armies from own territory not from {origin}"
    assert destination.player == player, f"Can only move armies to own territory not to {destination}"
    assert armies < origin.armies, f"The amount of armies should be less than armies on the origin position, not " \
                                   f"{armies}"


def execute_free_move(armies: int, origin: Territory, destination: Territory, player: Player):
    verify_free_move(armies, origin, destination, player)
    origin.armies -= armies
    destination.armies += armies


class Game:
    def __init__(self, players: [Player], board: Board):
        self.players: [Player] = players
        self.defeated_players: [Player] = []
        for i, player in enumerate(self.players):
            player.id = i

        self.board: Board = board
        self.game_over = False

        self.armies = len(players) * [180]  # The amount of armies in the box per player

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
            assert self.armies[player.id] >= armies_per_players, "Not enough armies in the box."
            self.armies[player.id] -= armies_per_players

        # Decide who gets to go first
        print("Highest roller gets to place it's armies first!\n")
        player = self.players[first_player(self.players)]
        print(f"{player.name.capitalize()} may begin!\n")

        self.board.print_board(0)
        while self.board.free_territories:
            assert self.armies[player.id] >= 0, "Not enough armies in the box."
            territory = player.claim_territory(self.board)
            extra_info = f"{player.name} claimed {self.board.free_territories[territory].name}"
            self.board.claim_territory(territory, player)
            self.board.print_board(0, [extra_info])
            player = self.players[(player.id + 1) % len(self.players)]

        self.board.print_board(1, ["-- SETUP COMPLETE --"])

    def accumulate_armies(self, player: Player):
        if self.armies[player.id] == 0:
            self.board.print_board(1, ['No more armies available in the box.'])
            return

        armies = min(self.armies[player.id], max(3, len(player.territories) // 3))

        extra_info = [f'{player.name.capitalize()} receives {armies} armies.']

        if self.armies[player.id] <= 3:
            player.armies += armies
            self.armies[player.id] -= armies
            return

        for continent in player.continents:
            extra = self.board.armies_per_continent[continent]
            if extra < self.armies[player.id]:
                armies += extra
                extra_info.append(
                    f'{player.name.capitalize()} receives {extra} armies for occupying the entirety of {continent.name}!')
            else:
                extra_info.append(f'Not enough armies in the box.')

        player.armies += armies
        self.armies[player.id] -= armies
        extra_info.append(
            f'{player.name.capitalize()} has received a total of {armies} armies. {player.name.capitalize()} now has '
            f'{player.armies} armies.')
        self.board.print_board(1, extra_info)

    def simulate_attack(self, player: Player, attack: int, attacker: Territory, defender: Territory):
        self.board.print_board(1, [f'{attacker.player.name} attacks {defender.name}!'])
        verify_attack(player, attack, attacker, defender)

        # Amount of dice used by the defender
        defense = defender.player.defend(attack, attacker, defender, self.board)
        verify_defense(defense, defender)

        (attacker_rolls, info_1) = dice.player_rolls_dices(attacker.player, attack)
        (defender_rolls, info_2) = dice.player_rolls_dices(defender.player, defense)
        attacker_rolls.sort()
        defender_rolls.sort()

        self.board.print_board(1, [info_1, info_2])

        attacker_losses = 0
        defender_losses = 0
        for i in range(min(len(attacker_rolls), len(defender_rolls))):
            if attacker_rolls[i] > defender_rolls[i]:
                defender_losses += 1
            else:
                attacker_losses += 1

        attacker.armies -= attacker_losses
        self.armies[attacker.player.id] += attacker_losses
        defender.armies -= defender_losses
        self.armies[defender.player.id] += defender_losses

        if defender.armies == 0:
            extra_info = [f'{player.name.capitalize()} has defeated all armies and captures {defender.name}!']
            defending_player = defender.player
            defender.player.territories.remove(defender)
            attacker.player.territories.add(defender)

            extra_info.append("Losses:")
            if attacker_losses > 0:
                extra_info.append(
                    f'    Attacker lost {attacker_losses} armies. {attacker.armies} remaining on {attacker.name}.')
            if defender_losses > 0:
                extra_info.append(
                    f'    Defender lost {defender_losses} armies. {defender.armies} remaingin on {defender.name}.')

            self.board.print_board(2, extra_info)
            extra_info = []

            defender.player = attacker.player
            capture = attacker.player.capture(attack, attacker, defender)
            assert capture >= attack, "You must move into the territory with at least as many armies as the number of dice rolled."
            assert capture < attacker.armies, "Not enough armies on territory. No territory may ever be left unoccupied at any time during the game."
            defender.armies = capture
            attacker.armies -= capture

            defender.continent.players[defender.player.id] -= 1
            defender.continent.players[attacker.player.id] += 1

            if defender.continent.players[attacker.player.id] == defender.continent.size:
                extra_info.append(f'{attacker.player.name} has taken over the entirety of {defender.continent.name}!')

            if len(defending_player.territories) == 0:
                extra_info.append(f'{defending_player.name.upper()} IS DEFEATED BY {attacker.player.name.upper()}!!')
                self.players.remove(defending_player)
                self.defeated_players.append(defending_player)

                # Check for game over
                if len(self.players) == 1:
                    self.game_over = True
                    winner = self.players[0]
                    for territory in self.board.territories:
                        assert territory.player == winner, f"Oops. Not all territories are occupied by the winner..."

                    extra_info.append(f'{winner.name.upper()} HAS WON THE GAME!!!')
            self.board.print_board(1, extra_info)

        else:
            self.board.print_board(1, [f'{player.name.capitalize()} was not able to take {defender.name}.'])

    def play(self):
        print("Highest roller gets to go play first!\n")
        player = first_player(self.players)
        print(f"{self.players[player].name.capitalize()} may begin!\n")

        turn = 1
        current_player = self.players[player]
        while not self.game_over:
            extra_info = [f'TURN {turn}:', f'{current_player.name}']
            turn += 1

            extra_info.append("Army Accumulation:")
            self.accumulate_armies(current_player)

            extra_info.append("Army Placement:")
            army_placement = current_player.place_armies(self.board)
            if len(army_placement) == 0:
                extra_info.append("No armies placed.")
            else:
                extra_info.append(f'{current_player.name.capitalize()} places armies on:')
            for (armies, territory) in army_placement:
                extra_info.append(f'    {territory.name}: {armies}')
                self.board.place_armies(territory, current_player, armies)

            self.board.print_board(1, extra_info)

            attack = current_player.attack(self.board)
            while attack is not None:
                (die, attacker, defender) = attack
                self.simulate_attack(current_player, die, attacker, defender)
                attack = current_player.attack(self.board)

            free_move = current_player.free_move(self.board)
            if free_move is not None:
                self.board.print_board(1, [f"{current_player.name} uses a free move."])
                (armies, origin, destination) = free_move
                execute_free_move(armies, origin, destination, current_player)
                self.board.print_board(1, [f"Moved {armies} from {origin.name} to {destination.name}."])

            player += 1
            player %= len(self.players)
            current_player = self.players[player]
