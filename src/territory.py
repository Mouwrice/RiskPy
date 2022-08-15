from continent import Continent


class Territory:
    def __init__(self, number: int, name: str, continent: Continent):
        self.id = number
        self.name = name
        self.abbr = self.name.upper()[:5]
        self.connections: [Territory] = []
        self.continent = continent
        self.armies = 0
        self.player = None

    def __str__(self):
        return (
            f"{self.name}\n"
            f"   id: {self.id}\n"
            f"   continent: {self.continent.name}\n"
            f"   armies: {self.armies}\n"
            f"   player: {str(self.player)}\n"
        )
