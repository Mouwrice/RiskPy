import random

from player import Player
from util import print_verbose


def roll_dices(amount: int) -> [int]:
    """
    Simulates rolling a given amount of standard 6 sided dices
    :param amount: The amount of dices to roll
    :returns: A list of dice rolls
    """
    return random.choices(range(1, 7), k=amount)


def player_rolls_dices(player: Player, amount: int) -> ([int], str):
    """
    Lets a player roll a given amount of standard 6 sided dices
    :param player: The player that rolls the dice
    :param amount: The amount of dices used
    :returns: A tuple of (a list of dice rolls, a textual result)
    """
    rolls = roll_dices(amount)
    joined = ', '.join([str(roll) for roll in rolls])
    return rolls, f"{player.name.capitalize()} rolls {amount} {'dice' if amount > 1 else 'die'}: {joined}"


def players_roll_dice(players: [Player], verbose: bool) -> [int]:
    """
    Rolls a standard 6 sided dice for every player
    :param players: List of players to roll dices for
    :param verbose: True if it should print the results to the console
    :returns: A list of dice rolls
    """
    rolls = roll_dices(len(players))
    for i, player in enumerate(players):
        print_verbose(f"{player.name.capitalize()} rolled {rolls[i]}.\n", verbose)
    return rolls
