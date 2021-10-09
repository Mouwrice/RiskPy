class Continent:
    def __init__(self, name: str, players: int, size: int):
        self.name = name
        self.players = players * [0]
        self.size = size
