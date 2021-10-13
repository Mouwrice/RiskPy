from board import ClassicBoard
from game import Game
from random_player import RandomPlayer


def main():
    board = ClassicBoard(4)
    game = Game([RandomPlayer("Player 1", 1, "\033[91m"), RandomPlayer("Player 2", 2, "\033[92m"),
                 RandomPlayer("Player 3", 3, "\033[93m"),
                 RandomPlayer("Player 4", 4, "\033[94m")], board)
    game.setup()
    game.play()


if __name__ == '__main__':
    main()
