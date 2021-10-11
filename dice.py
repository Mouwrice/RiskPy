import random

from player import Player


def roll_dices(amount: int):
    return [random.randint(1, 6) for _ in range(amount)]


def players_roll_dice(players: [Player]):
    rolls = roll_dices(len(players))
    for i, player in enumerate(players):
        print(f"{player.name.capitalize()} rolled {rolls[i]}.")
    print()
    return rolls
