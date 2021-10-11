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
        player = '/'
        if self.player:
            player = self.player
        armies = '/'
        if self.armies > 0:
            armies = self.armies
        return f'  ***** \n' \
               f'* {self.abbr} *\n' \
               f'* {player}   {armies} *\n' \
               f'  ***** '
