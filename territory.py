from continent import Continent


class Territory:
    def __init__(self, name: str, continent: Continent):
        self.name = name
        self.connections: [Territory] = []
        self.continent = continent
        self.armies = 0
