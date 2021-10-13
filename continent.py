class Continent:
    def __init__(self, number: int, name: str, players: int, size: int):
        self.id = number
        self.name = name
        self.players = players * [0]
        self.size = size
