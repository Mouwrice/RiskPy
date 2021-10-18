from board import ClassicBoard
from game import Game
from random_player import RandomPlayer, RandomPeacefulPlayer


def main():
    four_randoms = [RandomPlayer("Player 1", "\033[91m"), RandomPlayer("Player 2", "\033[92m"),
                    RandomPlayer("Player 3", "\033[93m"), RandomPlayer("Player 4", "\033[94m")]
    board = ClassicBoard(len(four_randoms))
    game = Game(four_randoms, board)
    game.setup()
    game.play()


if __name__ == '__main__':
    main()
