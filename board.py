from continent import Continent
from territory import Territory


def sanitize_territories(territories: [Territory]):
    ids = set()
    for territory in territories:
        assert territory.id not in ids, f'Territory id\'s should be unique. Found double id: {territory.id}'
        ids.add(territory.id)


def sanitize_continents(continents: [Continent]):
    ids = set()
    for continent in continents:
        assert continent.id not in ids, f'Continent id\'s should be unique. Found double id: {continent.id}'


class Board:
    def __init__(self, continents: [Continent], territories: [Territory]):
        sanitize_continents(continents)
        sanitize_territories(territories)
        self.continents = continents
        self.territories = territories
        self.free_territories = [territory for territory in territories]
        self.id_to_territory = dict()
        for territory in territories:
            self.id_to_territory[territory.id] = territory

        self.id_to_continent = dict()
        for continent in continents:
            self.id_to_continent[continent.id] = continent

        self.armies_per_continent = dict()

    def __str__(self):
        return '\n'.join([f'\n{self.id_to_territory[key].name}: {self.id_to_territory[key].continent.name} '
                          f'{[connection.name for connection in self.id_to_territory[key].connections]}\n'
                          + str(self.id_to_territory[key]) for key in
                          self.id_to_territory.keys()])

    def claim_territory(self, territory_index: int, player: 'Player'):
        territory_id = self.free_territories[territory_index].id
        player.armies -= 1
        player.territories.add(self.free_territories[territory_index])
        del self.free_territories[territory_index]
        territory = self.id_to_territory[territory_id]
        territory.player = player
        territory.armies = 1

        continent = self.id_to_continent[territory.continent.id]
        continent.players[player.id] += 1
        if continent.players[player.id] == continent.size:
            player.continents.add(continent)

    def place_armies(self, territory: Territory, player: 'Player', armies: int):
        assert self.id_to_territory[territory.id].player == player, "Territory is already occupied by another player!"
        assert armies <= player.armies, "Not enough armies!"
        territory.armies += armies
        player.armies -= armies


class ClassicBoard(Board):
    def __init__(self, players: int):
        # CONTINENTS
        north_america = Continent(1, "North America", players, 9)
        europe = Continent(2, "Europe", players, 6)
        asia = Continent(3, "Asia", players, 12)
        south_america = Continent(4, "South America", players, 4)
        africa = Continent(5, "Africa", players, 6)
        australia = Continent(6, "Australia", players, 4)

        # TERRITORIES

        # NORTH AMERICA
        alaska = Territory(1, "Alaska", north_america)
        northwest_territory = Territory(2, "Northwest Territory", north_america)
        greenland = Territory(3, "Greenland", north_america)
        alberta = Territory(4, "Alberta", north_america)
        ontario = Territory(5, "Ontario", north_america)
        quebec = Territory(6, "Quebec", north_america)
        western_us = Territory(7, "Western US", north_america)
        eastern_us = Territory(8, "Eastern US", north_america)
        central_america = Territory(9, "Central America", north_america)

        # SOUTH AMERICA
        venezuela = Territory(10, "Venezuela", south_america)
        brazil = Territory(11, "Brazil", south_america)
        peru = Territory(12, "Peru", south_america)
        argentina = Territory(13, "Argentina", south_america)

        # EUROPE
        iceland = Territory(14, "Iceland", europe)
        scandinavia = Territory(15, "Scandinavia", europe)
        great_britain = Territory(16, "Great Britain", europe)
        northern_europe = Territory(17, "Northern Europe", europe)
        ukraine = Territory(18, "Ukraine", europe)
        western_europe = Territory(19, "Western Europe", europe)
        southern_europe = Territory(20, "Southern Europe", europe)

        # ASIA
        yakutsk = Territory(21, "Yakutsk", asia)
        ural = Territory(22, "Ural", asia)
        siberia = Territory(23, "Siberia", asia)
        irkutsk = Territory(24, "Irkutsk", asia)
        kamchatka = Territory(25, "Kamcatka", asia)
        afghanistan = Territory(26, "Afghanistan", asia)
        china = Territory(27, "China", asia)
        mongolia = Territory(28, "Mongolia", asia)
        japan = Territory(29, "Japan", asia)
        middle_east = Territory(30, "Middle East", asia)
        india = Territory(31, "India", asia)
        siam = Territory(32, "Siam", asia)

        # AFRICA
        north_africa = Territory(33, "North Africa", africa)
        egypt = Territory(34, "Egypt", africa)
        congo = Territory(35, "Congo", africa)
        east_africa = Territory(36, "East Africa", africa)
        south_africa = Territory(37, "South Africa", africa)
        madagascar = Territory(38, "Madagascar", africa)

        # AUSTRALIA
        indonesia = Territory(39, "Indonesia", australia)
        new_guinea = Territory(40, "New Guinea", australia)
        western_australia = Territory(41, "Western Australia", australia)
        eastern_australia = Territory(42, "Eastern Australia", australia)

        # CONNECTIONS
        alaska.connections = [northwest_territory, alberta, kamchatka]
        northwest_territory.connections = [alaska, greenland, alberta, ontario]
        greenland.connections = [northwest_territory, iceland, ontario, quebec]
        alberta.connections = [alaska, northwest_territory, ontario, western_us]
        ontario.connections = [alberta, northwest_territory, greenland, quebec, western_us, eastern_us]
        quebec.connections = [ontario, greenland, eastern_us]
        western_us.connections = [alberta, ontario, eastern_us, central_america]
        eastern_us.connections = [western_us, central_america, quebec, ontario]
        central_america.connections = [western_us, eastern_us, venezuela]

        venezuela.connections = [central_america, brazil, peru]
        brazil.connections = [venezuela, peru, argentina, north_africa]
        peru.connections = [venezuela, brazil, argentina]
        argentina.connections = [peru, brazil]

        iceland.connections = [greenland, scandinavia, great_britain]
        scandinavia.connections = [iceland, great_britain, northern_europe, ukraine]
        great_britain.connections = [iceland, scandinavia, northern_europe, western_europe]
        northern_europe.connections = [great_britain, scandinavia, ukraine, western_europe, southern_europe]
        ukraine.connections = [scandinavia, northern_europe, southern_europe, ural, afghanistan, middle_east]
        western_europe.connections = [north_africa, great_britain, northern_europe, southern_europe]
        southern_europe.connections = [northern_europe, ukraine, western_europe, middle_east, north_africa, egypt]

        yakutsk.connections = [siberia, irkutsk, kamchatka]
        ural.connections = [ukraine, afghanistan, china, siberia]
        siberia.connections = [ural, afghanistan, china, mongolia, irkutsk, yakutsk]
        irkutsk.connections = [siberia, mongolia, kamchatka, yakutsk]
        kamchatka.connections = [yakutsk, irkutsk, mongolia, japan, alaska]
        afghanistan.connections = [ural, ukraine, middle_east, india, china]
        china.connections = [afghanistan, india, siam, mongolia, siberia, ural]
        mongolia.connections = [china, japan, kamchatka, irkutsk, siberia]
        japan.connections = [mongolia, kamchatka]
        middle_east.connections = [afghanistan, ukraine, southern_europe, egypt, east_africa, india]
        india.connections = [middle_east, siam, china, afghanistan]
        siam.connections = [china, india, indonesia]

        north_africa.connections = [western_europe, southern_europe, brazil, congo, east_africa, egypt]
        egypt.connections = [north_africa, east_africa, middle_east, southern_europe]
        congo.connections = [north_africa, south_africa, east_africa]
        east_africa.connections = [north_africa, congo, south_africa, madagascar, middle_east, egypt]
        south_africa.connections = [congo, east_africa, madagascar]
        madagascar.connections = [south_africa, east_africa]

        indonesia.connections = [siam, new_guinea, western_australia]
        new_guinea.connections = [indonesia, western_australia, eastern_australia]
        western_australia.connections = [indonesia, new_guinea, eastern_australia]
        eastern_australia.connections = [western_australia, new_guinea]

        continents = [north_america, south_america, europe, asia, africa, australia]

        super().__init__(continents,
                         [alaska, northwest_territory, greenland, alberta, ontario, quebec, western_us, eastern_us,
                          central_america, venezuela, brazil, peru, argentina, iceland, scandinavia, great_britain,
                          northern_europe, ukraine, western_europe, southern_europe, yakutsk, ural, siberia, irkutsk,
                          kamchatka, afghanistan, china, mongolia, japan, middle_east, india, siam, north_africa,
                          egypt,
                          congo, east_africa, south_africa, madagascar, indonesia, new_guinea, western_australia,
                          eastern_australia])

        self.armies_per_continent[north_america] = 5
        self.armies_per_continent[south_america] = 2
        self.armies_per_continent[europe] = 5
        self.armies_per_continent[asia] = 7
        self.armies_per_continent[africa] = 3
        self.armies_per_continent[australia] = 2

    def __str__(self):
        # player per territory
        t = []
        v = []
        h = []
        for territory in self.territories:
            if territory.player is None:
                t.append("/   / ")
                v.append("*")
                h.append("*****")
            else:
                v.append(territory.player.colorize_text("*"))
                h.append(territory.player.colorize_text("*****"))
                t.append(str(territory.player.id) + (4 - len(str(territory.armies))) * " " + str(territory.armies) + " ")

        return f'         +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n' \
               f'         |                                                                                                                                                                       |\n' \
               f'  # # #  |  # # # # # # # # # # # # # # # # # # #                                                                                                        # # # # # # # # # # #   |\n' \
               f' #       |                                       #                                                                                                      #                     #  |\n' \
               f'#      {h[0]}           {h[1]}           {h[2]}      #                                                                                                    #       {h[20]}             |\n' \
               f'#    {v[0]} ALASK {v[0]} ----- {v[1]} NORTH {v[1]} ----- {v[2]} GREEN {v[2]} -----+                  ..........                                               ........              #      {v[20]} YAKUT {v[20]}           |  #\n' \
               f'#    {v[0]} {t[0]}{v[0]}       {v[1]} {t[1]}{v[1]}       {v[2]} {t[2]}{v[2]}    #  \\                 . EUROPE .                                               . ASIA .             #       {v[20]} {t[20]}{v[20]}           |    #\n' \
               f'#      {h[0]}       /   {h[1]}       /   {h[2]}      #   \\                ..........                                               ........            #      /   {h[20]}   \\         |     #\n' \
               f'#        |        /      |        /      |        #    \\                                                                                           #      /      |      \\        |      #\n' \
               f'#        |       /       |       /       |        #     \\     # # # # # # # # # # # # # # # #                             # # # # # # # # # # # # #      /       |       \\       |       #\n' \
               f'#        |      /        |      /        |        #      \\   #                               #                           #                              /        |        \\      |       #\n' \
               f'#      {h[3]}   /       {h[4]}   /       {h[5]}      #       \\ #      {h[13]}           {h[14]}      #                          #     {h[21]}           {h[22]}   /       {h[23]}       \\   {h[24]}     #\n' \
               f'#    {v[3]} ALBER {v[3]} ----- {v[4]} ONTAR {v[4]} ----- {v[5]} QUEBE {v[5]}    #        ----- {v[13]} ICELA {v[13]} ----- {v[14]} SCAND {v[14]}     #                      +----- {v[21]} URAL  {v[21]} ----- {v[22]} SIBER {v[22]} ----- {v[23]} IRKUT {v[23]} ----- {v[24]} KAMCA {v[24]}   #\n' \
               f'#    {v[3]} {t[3]}{v[3]}       {v[4]} {t[4]}{v[4]}       {v[5]} {t[5]}{v[5]}    #         #    {v[13]} {t[13]}{v[13]}       {v[14]} {t[14]}{v[14]}     #                     /   #   {v[21]} {t[21]}{v[21]}       {v[22]} {t[22]}{v[22]}       {v[23]} {t[23]}{v[23]}       {v[24]} {t[24]}{v[24]}   #\n' \
               f'#      {h[3]}       /   {h[4]}       /   {h[5]}      #         #      {h[13]}       /   {h[14]}   \\     #                  /    #     {h[21]}   \\       {h[22]}   \\       {h[23]}       /   {h[24]}     #\n' \
               f'#        |        /      |        /              #          #        |        /      |      \\     #                /     #       |      \\        |      \\        |        /      |       #\n' \
               f'#        |       /       |       /     # # # # #            #        |       /       |       \\     # # # # #      /      #       |       \\       |       \\       |       /       |       #\n' \
               f'#        |      /        |      /     #                     #        |      /        |        \\             #    /       #       |        \\      |        \\      |      /        |       #\n' \
               f'#      {h[6]}   /       {h[7]}   /     #                      #      {h[15]}   /       {h[16]}       \\   {h[17]}     #  /        #     {h[25]}       \\   {h[26]}       \\   {h[27]}   /       {h[28]}     #\n' \
               f'#    {v[6]} WESTE {v[6]} ----- {v[7]} EASTE {v[7]}      #                       #    {v[15]} GREAT {v[15]} ----- {v[16]} NORTH {v[16]} ----- {v[17]} UKRAI {v[17]} ----+------------ {v[25]} AFGHA {v[25]} ----- {v[26]} CHINA {v[26]} ----- {v[27]} MONGO {v[27]} ----- {v[28]} JAPAN {v[28]}   #\n' \
               f'#    {v[6]} {t[6]}{v[6]}       {v[7]} {t[7]}{v[7]}     #                        #    {v[15]} {t[15]}{v[15]}       {v[16]} {t[16]}{v[16]}       {v[17]} {t[17]}{v[17]}    # \\        #   {v[25]} {t[25]}{v[25]}       {v[26]} {t[26]}{v[26]}       {v[27]} {t[27]}{v[27]}       {v[28]} {t[28]}{v[28]}   #\n' \
               f'#      {h[6]}       /   {h[7]}      #                         #      {h[15]}   \\       {h[16]}   \\       {h[17]}      #  \\       #     {h[25]}   \\       {h[26]}   \\       {h[27]}           {h[28]}     #\n' \
               f'#        |        /              #                          #               \\        |      \\        |        #   \\      #       |      \\        |      \\        |                      #\n' \
               f'#        |       /     # # # # #                             #               \\       |       \\       |        #    \\     #       |       \\       |       \\       |           # # # # # #\n' \
               f'#        |      /     #                                       #               \\      |        \\      |        #     \\    #       |        \\      |        \\      |          #\n' \
               f'#      {h[8]}   /     #   .................                     #               \\   {h[18]}       \\   {h[19]}      #      \\   #     {h[29]}       \\   {h[30]}       \\   {h[31]}       #\n' \
               f'#    {v[8]} CENTR {v[8]}      #    . NORTH AMERICA .                      #                {v[18]} WESTE {v[18]} ----- {v[19]} SOUTH {v[19]} -----------+----- {v[29]} MIDDL {v[29]} ----- {v[30]} INDIA {v[30]} ----- {v[31]} SIAM  {v[31]}    #\n' \
               f'#    {v[8]} {t[8]}{v[8]}     #     .................                       #               {v[18]} {t[18]}{v[18]}       {v[19]} {t[19]}{v[19]}    #      /   #   {v[29]} {t[29]}{v[29]}       {v[30]} {t[30]}{v[30]}       {v[31]} {t[31]}{v[31]}   #\n' \
               f'#      {h[8]}      #                                               #                {h[18]}        /  {h[19]}      #     /      /   {h[29]}           {h[30]}           {h[31]}    #\n' \
               f' #       |       #                                                 #                 |         /     |      #      /      /                                      |     #\n' \
               f'  # # #  |  # # #                                                   # # # # # # # #  |  # #   /   #  |  # #       /      /  # # # # # # # # # # # # # # # # # #  |  # #\n' \
               f'         |                                                                           |       /       |           /      /                                        |\n' \
               f'  # # #  |  # # # # # # # # # # #                                             # # #  |  #   /  # #   |  # # #   /      /                                  # # #  | # # # # # # # # # # # #\n' \
               f' #       |                       #                                           #       |     /         |       # /      /                                 #        |                        #\n' \
               f'#      {h[9]}           {h[10]}     #                                          #      {h[32]}  /        {h[33]}      /      /                                  #      {h[38]}           {h[39]}      #\n' \
               f'#    {v[9]} VENEZ {v[9]} ----- {v[10]} BRAZI {v[10]} ------------------------------------------------- {v[32]} NORTH {v[32]} ----- {v[33]} EGYPT {v[33]} --+      /                                   #    {v[38]} INDON {v[38]} ----- {v[39]} NEW G {v[39]}    #\n' \
               f'#    {v[9]} {t[9]}{v[9]}       {v[10]} {t[10]}{v[10]}    #                                         #    {v[32]} {t[32]}{v[32]}       {v[33]} {t[33]}{v[33]}    #    /                   .............    #    {v[38]} {t[38]}{v[38]}       {v[39]} {t[39]}{v[39]}    #\n' \
               f'#      {h[9]}       /   {h[10]}      #                                         #      {h[32]}   \\       {h[33]}      #   /                    . AUSTRALIA .    #      {h[38]}       /   {h[39]}      #\n' \
               f'#        |        /      |        #                                         #        |      \\        |        #  /                     .............    #        |        /      |        #\n' \
               f'#        |       /       |        #                                         #        |       \\       |        # /                                       #        |       /       |        #\n' \
               f'#        |      /        |        #                                         #        |        \\      |         /                                        #        |      /        |        #\n' \
               f'#      {h[11]}   /       {h[12]}      #   .................                     #      {h[34]}       \\   {h[35]}      /                                         #       {h[40]}   /       {h[41]}     #\n' \
               f'#    {v[11]} PERU  {v[11]} ----- {v[12]} ARGEN {v[12]}    #   . SOUTH AMERICA .                     #    {v[34]} CONGO {v[34]} ----- {v[35]} EAST  {v[35]} --+                                          #     {v[40]} WESTE {v[40]} ----- {v[41]} EASTE {v[41]}   #\n' \
               f'#    {v[11]} {t[11]}{v[11]}       {v[12]} {t[12]}{v[12]}    #   .................                     #    {v[34]} {t[34]}{v[34]}       {v[35]} {t[35]}{v[35]}    #                                         #     {v[40]} {t[40]}{v[40]}       {v[41]} {t[41]}{v[41]}   #\n' \
               f'#      {h[11]}           {h[12]}      #                                         #      {h[34]}       /   {h[35]}      #                                         #       {h[40]}           {h[41]}     #\n' \
               f' #                               #                                          #        |        /      |        #                                         #                                 #\n' \
               f'  # # # # # # # # # # # # # # # #                                           #        |       /       |        #                                           # # # # # # # # # # # # # # # #\n' \
               f'                                                                            #        |      /        |        #\n' \
               f'                                                                            #      {h[36]}   /       {h[37]}      #   ..........\n' \
               f'                                                                            #    {v[36]} SOUTH {v[36]} ----- {v[37]} MADAG {v[37]}    #   . AFRICA .\n' \
               f'                                                                            #    {v[36]} {t[36]}{v[36]}       {v[37]} {t[37]}{v[37]}    #   ..........\n' \
               f'                                                                            #      {h[36]}           {h[37]}      #\n' \
               f'                                                                             #                               #\n' \
               f'                                                                               # # # # # # # # # # # # # # #\n'
