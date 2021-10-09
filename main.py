from board import ClassicBoard


def main():
    board = ClassicBoard(4)
    for territory in board.territories:
        print(f'{territory.name}: {territory.continent.name} {[connection.name for connection in territory.connections]}')


if __name__ == '__main__':
    main()
