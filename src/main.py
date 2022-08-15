from board import ClassicBoard
from game import Game
from random_player import RandomPlayer, RandomPeacefulPlayer, RandomHostilePlayer


def main():
    players = [RandomPlayer("Player 1", "\033[91m"), RandomPlayer("Player 2", "\033[92m"),
               RandomPlayer("Player 3", "\033[93m"), RandomPlayer("Player 4", "\033[94m")]
    board = ClassicBoard(len(players))
    game = Game(players, board)
    game.setup(False)
    game.play(verbose=False, max_turns=100000)


if __name__ == '__main__':
    main()
