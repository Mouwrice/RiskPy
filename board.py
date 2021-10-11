from continent import Continent
from territory import Territory


def sanitize_territories(territories: [Territory]):
    ids = set()
    for territory in territories:
        assert territory.id not in ids, f'Territory id\'s should be unique. Found double id: {territory.id}'
        ids.add(territory.id)


class Board:
    def __init__(self, territories: [Territory]):
        sanitize_territories(territories)
        self.territories: [Territory] = territories
        self.free_territories = [territory for territory in territories]
        self.id_to_territory = dict()
        for territory in territories:
            self.id_to_territory[territory.id] = territory

    def __str__(self):
        return '\n'.join([f'\n{self.id_to_territory[key].name}: {self.id_to_territory[key].continent.name} '
                          f'{[connection.name for connection in self.id_to_territory[key].connections]}\n'
                          + str(self.id_to_territory[key]) for key in
                          self.id_to_territory.keys()])

    def claim_territory(self, territory: int, player: 'Player'):
        territory_id = self.free_territories[territory].id
        del self.free_territories[territory]
        self.id_to_territory[territory_id].player = player
        self.id_to_territory[territory_id].armies = 1

    def place_armies(self, territory: Territory, player: 'Player', armies: int):
        if self.id_to_territory[territory.id].playerPlayer == player:
            territory.armies += armies
            return

        print("Territory is already occupied by another player!")


class ClassicBoard(Board):
    def __init__(self, players: int):
        # CONTINENTS
        north_america = Continent("North America", players, 9)
        europe = Continent("Europe", players, 6)
        asia = Continent("Asia", players, 12)
        south_america = Continent("South America", players, 4)
        africa = Continent("Africa", players, 6)
        australia = Continent("Australia", players, 4)

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

        super().__init__([alaska, northwest_territory, greenland, alberta, ontario, quebec, western_us, eastern_us,
                          central_america, venezuela, brazil, peru, argentina, iceland, scandinavia, great_britain,
                          northern_europe, ukraine, western_europe, southern_europe, yakutsk, ural, siberia, irkutsk,
                          kamchatka, afghanistan, china, mongolia, japan, middle_east, india, siam, north_africa, egypt,
                          congo, east_africa, south_africa, madagascar, indonesia, new_guinea, western_australia,
                          eastern_australia])

    def __str__(self):
        # player per territory
        p = [territory.player.id for territory in self.territories]
        # armies per territory
        a = [(4 - territory.armies) * " " + str(territory.armies) for territory in self.territories]

        return f'         +-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+\n' \
            f'         |                                                                                                                                                                       |\n' \
            f'  # # #  |  # # # # # # # # # # # # # # # # # # #                                                                                                        # # # # # # # # # # #   |\n' \
            f' #       |                                       #                                                                                                      #                     #  |\n' \
            f'#      *****           *****           *****      #                                                                                                    #       *****             |\n' \
            f'#    * ALASK * ----- * NORTH * ----- * GREEN * -----+                  ..........                                               ........              #      * YAKUT *           |  #\n' \
            f'#    * {p[0]}{a[0]} *       * /   / *       * /   / *    #  \                 . EUROPE .                                               . ASIA .             #       * /   / *           |    #\n' \
            f'#      *****       /   *****       /   *****      #   \                ..........                                               ........            #      /   *****   \         |     #\n' \
            f'#        |        /      |        /      |        #    \                                                                                           #      /      |      \        |      #\n' \
            f'#        |       /       |       /       |        #     \     # # # # # # # # # # # # # # # #                             # # # # # # # # # # # # #      /       |       \       |       #\n' \
            f'#        |      /        |      /        |        #      \   #                               #                           #                              /        |        \      |       #\n' \
            f'#      *****   /       *****   /       *****      #       \ #      *****           *****      #                          #     *****           *****   /       *****       \   *****     #\n' \
            f'#    * ALBER * ----- * ONTAR * ----- * QUEBE *    #        ----- * ICELA * ----- * SCAND *     #                      +----- * URAL  * ----- * SIBER * ----- * IRKUT * ----- * KAMCA *   #\n' \
            f'#    * /   / *       * /   / *       * /   / *    #         #    * /   / *       * /   / *      #                    /   #   * /   / *       * /   / *       * /   / *       * /   / *   #\n' \
            f'#      *****       /   *****       /   *****      #         #      *****       /   *****   \     #                  /    #     *****   \       *****   \       *****       /   *****     #\n' \
            f'#        |        /      |        /              #          #        |        /      |      \     #                /     #       |      \        |      \        |        /      |       #\n' \
            f'#        |       /       |       /     # # # # #            #        |       /       |       \     # # # # #      /      #       |       \       |       \       |       /       |       #\n' \
            f'#        |      /        |      /     #                     #        |      /        |        \             #    /       #       |        \      |        \      |      /        |       #\n' \
            f'#      *****   /       *****   /     #                      #      *****   /       *****       \   *****     #  /        #     *****       \   *****       \   *****   /      *****      #\n' \
            f'#    * WESTE * ----- * EASTE *      #                       #    * GREAT * ----- * NORTH * ----- * UKRAI * ----+------------ * AFGHA * ----- * CHINA * ----- * MONGO * ----- * JAPAN *   #\n' \
            f'#    * /   / *       * /   / *     #                        #    * /   / *       * /   / *       * /   / *    # \        #   * /   / *       * /   / *       * /   / *       * /   / *   #\n' \
            f'#      *****       /   *****      #                         #      *****   \       *****   \       *****      #  \       #     *****   \       *****   \       *****          *****      #\n' \
            f'#        |        /              #                          #               \        |      \        |        #   \      #       |      \        |      \        |                      #\n' \
            f'#        |       /     # # # # #                             #               \       |       \       |        #    \     #       |       \       |       \       |           # # # # # #\n' \
            f'#        |      /     #                                       #               \      |        \      |        #     \    #       |        \      |        \      |          #\n' \
            f'#      *****   /     #   .................                     #               \   *****       \   *****      #      \   #     *****       \   *****       \   *****       #\n' \
            f'#    * CENTR *      #    . NORTH AMERICA .                      #                * WESTE * ----- * SOUTH * -----------+----- * MIDDL * ----- * INDIA * ----- * SIAM  *    #\n' \
            f'#    * /   / *     #     .................                       #               * /   / *       * /   / *    #      /   #   * /   / *       * /   / *       * /   / *   #\n' \
            f'#      *****      #                                               #                *****        /  *****      #     /      /   *****          ******           *****    #\n' \
            f' #       |       #                                                 #                 |         /     |      #      /      /                                      |     #\n' \
            f'  # # #  |  # # #                                                   # # # # # # # #  |  # #   /   #  |  # #       /      /  # # # # # # # # # # # # # # # # # #  |  # #\n' \
            f'         |                                                                           |       /       |           /      /                                        |\n' \
            f'  # # #  |  # # # # # # # # # # #                                             # # #  |  #   /  # #   |  # # #   /      /                                  # # #  | # # # # # # # # # # # #\n' \
            f' #       |                       #                                           #       |     /         |       # /      /                                 #        |                        #\n' \
            f'#      *****           *****      #                                         #      *****  /        *****      /      /                                  #      *****           *****      #\n' \
            f'#    * VENEZ * ----- * BRAZI * ------------------------------------------------- * NORTH * ----- * EGYPT * --+      /                                   #    * INDON * ----- * NEW G *    #\n' \
            f'#    * /   / *       * /   / *    #                                         #    * /   / *       * /   / *    #    /                   .............    #    * /   / *       * /   / *    #\n' \
            f'#      *****       /   *****      #                                         #      *****   \      *****       #   /                    . AUSTRALIA .    #      *****       /   *****      #\n' \
            f'#        |        /      |        #                                         #        |      \        |        #  /                     .............    #        |        /      |        #\n' \
            f'#        |       /       |        #                                         #        |       \       |        # /                                       #        |       /       |        #\n' \
            f'#        |      /        |        #                                         #        |        \      |         /                                        #        |      /        |        #\n' \
            f'#      *****   /       *****      #   .................                     #      *****       \   *****      /                                         #      *****   /       *****      #\n' \
            f'#    * PERU  * ----- * ARGEN *    #   . SOUTH AMERICA .                     #    * CONGO * ----- * EAST  * --+                                          #     * WESTE * ----- * EASTE *   #\n' \
            f'#    * /   / *       * /   / *    #   .................                     #    * /   / *       * /   / *    #                                         #     * /   / *       * /   / *   #\n' \
            f'#      *****           *****      #                                         #      *****       /   *****      #                                         #       *****           *****     #\n' \
            f' #                               #                                          #        |        /      |        #                                         #                                 #\n' \
            f'  # # # # # # # # # # # # # # # #                                           #        |       /       |        #                                           # # # # # # # # # # # # # # # #\n' \
            f'                                                                            #        |      /        |        #\n' \
            f'                                                                            #      *****   /       *****      #   ..........\n' \
            f'                                                                            #    * SOUTH * ----- * MADAG *    #   . AFRICA .\n' \
            f'                                                                            #    * /   / *       * /   / *    #   ..........\n' \
            f'                                                                            #      *****           *****      #\n' \
            f'                                                                             #                               #\n' \
            f'                                                                               # # # # # # # # # # # # # # #\n'
