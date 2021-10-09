from continent import Continent
from territory import Territory


class Board:
    def __init__(self, territories: [Territory], players: int):
        self.territories: [Territory] = territories


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
        alaska = Territory("Alaska", north_america)
        northwest_territory = Territory("Northwest Territory", north_america)
        greenland = Territory("Greenland", north_america)
        alberta = Territory("Alberta", north_america)
        ontario = Territory("Ontario", north_america)
        quebec = Territory("Quebec", north_america)
        western_us = Territory("Western US", north_america)
        eastern_us = Territory("Eastern US", north_america)
        central_america = Territory("Central America", north_america)

        # SOUTH AMERICA
        venezuela = Territory("Venezuela", south_america)
        brazil = Territory("Brazil", south_america)
        peru = Territory("Peru", south_america)
        argentina = Territory("Argentina", south_america)

        # EUROPE
        iceland = Territory("Iceland", europe)
        scandinavia = Territory("Scandinavia", europe)
        great_britain = Territory("Great Britain", europe)
        northern_europe = Territory("Northern Europe", europe)
        ukraine = Territory("Ukraine", europe)
        western_europe = Territory("Western Europe", europe)
        southern_europe = Territory("Southern Europe", europe)

        # ASIA
        yakutsk = Territory("Yakutsk", asia)
        ural = Territory("Ural", asia)
        siberia = Territory("Siberia", asia)
        irkutsk = Territory("Irkutsk", asia)
        kamchatka = Territory("Kamcatka", asia)
        afghanistan = Territory("Afghanistan", asia)
        china = Territory("China", asia)
        mongolia = Territory("Mongolia", asia)
        japan = Territory("Japan", asia)
        middle_east = Territory("Middle East", asia)
        india = Territory("India", asia)
        siam = Territory("Siam", asia)

        # AFRICA
        north_africa = Territory("North Africa", africa)
        egypt = Territory("Egypt", africa)
        congo = Territory("Congo", africa)
        east_africa = Territory("East Africa", africa)
        south_africa = Territory("South Africa", africa)
        madagascar = Territory("Madagascar", africa)

        # AUSTRALIA
        indonesia = Territory("Indonesia", australia)
        new_guinea = Territory("New Guinea", australia)
        western_australia = Territory("Western Australia", australia)
        eastern_australia = Territory("Eastern Australia", australia)

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
                          eastern_australia], players)
