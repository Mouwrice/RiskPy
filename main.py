from board import ClassicBoard
from game import Game
from random_player import RandomPlayer


def main():
    board = ClassicBoard(4)
    game = Game([RandomPlayer("Player 1", 1), RandomPlayer("Player 2", 2), RandomPlayer("Player 3", 3),
                 RandomPlayer("Player 4", 4)], board)
    game.setup()


if __name__ == '__main__':
    main()
