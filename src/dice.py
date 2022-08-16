import random

from player import Player
from util import print_verbose


def roll_dice(amount: int) -> [int]:
    """
    Simulates rolling a given amount of standard 6 sided dice
    :param amount: The amount of dice to roll
    :returns: A list of die rolls
    """
    return random.choices(range(1, 7), k=amount)


def player_rolls_dice(player: Player, amount: int) -> ([int], str):
    """
    Lets a player roll a given amount of standard 6 sided dice
    :param player: The player that rolls the die
    :param amount: The amount of dice used
    :returns: A tuple of (a list of die rolls, a textual result)
    """
    rolls = roll_dice(amount)
    joined = ", ".join([str(roll) for roll in rolls])
    return rolls, f"{player.name.capitalize()} rolls {amount} {'dice' if amount > 1 else 'die'}: {joined}"


def players_roll_die(players: [Player], verbose: bool) -> [int]:
    """
    Rolls a standard 6 sided die for every player
    :param players: List of players to roll dice for
    :param verbose: True if it should print the results to the console
    :returns: A list of die rolls
    """
    rolls = roll_dice(len(players))
    for i, player in enumerate(players):
        print_verbose(f"{player.name.capitalize()} rolled {rolls[i]}.\n", verbose)
    return rolls
