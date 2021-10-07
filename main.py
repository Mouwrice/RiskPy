from enum import Enum, auto


class Contintent(Enum):
    NORTH_AMERICA = auto
    SOUTH_AMERICA = auto
    EUROPE = auto
    ASIA = auto
    AFRICA = auto
    AUSTRALIA = auto


class Territory:
    def __init__(self, name: str, continent: Contintent):
        self.name = name
        self.connections: [Territory] = []
        self.continent = continent
        self.armies = 0


class Board:
    def __init__(self, territories: [Territory]):
        self.territories: [Territory] = territories


alaska = Territory("Alaska", Contintent.NORTH_AMERICA)
northwest_territory = Territory("Northwest Territory", Contintent.NORTH_AMERICA)
greenland = Territory("Greenland", Contintent.NORTH_AMERICA)

alaska.connections = [northwest_territory]
northwest_territory.connections = [alaska, greenland]
greenland.connections = [northwest_territory]


def main():
    board = Board([alaska, northwest_territory, greenland])
    for territory in board.territories:
        print(f'{territory.name}: {territory.continent} {[connection.name for connection in territory.connections]}')


if __name__ == '__main__':
    main()
