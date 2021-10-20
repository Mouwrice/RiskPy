import random

from player import Player


def roll_dices(amount: int):
    return [random.randint(1, 6) for _ in range(amount)]


def player_rolls_dices(player: Player, amount: int):
    rolls = roll_dices(amount)
    joined = ', '.join([str(roll) for roll in rolls])
    print(f"{player.name.capitalize()} rolls {amount} {'dice' if amount > 1 else 'die'}: {joined}")
    return rolls


def players_roll_dice(players: [Player]):
    rolls = roll_dices(len(players))
    for i, player in enumerate(players):
        print(f"{player.name.capitalize()} rolled {rolls[i]}.")
    print()
    return rolls
