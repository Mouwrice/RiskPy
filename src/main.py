from board import ClassicBoard
from game import Game
from random_player import RandomPlayer, RandomPeacefulPlayer, RandomHostilePlayer


def main():
    players = [  # RandomPlayer("Player 1", "\033[91m"), RandomPlayer("Player 2", "\033[92m"),
                    RandomHostilePlayer("Player 3", "\033[93m"), RandomPeacefulPlayer("Player 4", "\033[94m")]
    board = ClassicBoard(len(players))
    game = Game(players, board)
    game.setup()
    game.play()


if __name__ == '__main__':
    main()
