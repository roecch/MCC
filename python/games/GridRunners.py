from python.games.GameInterface import GameInterface
from python.games.GameAbstract import GameAbstract


class GridRunners(GameInterface):
    def __init__(self):
        self.startingPts = {"16": 150,
                            "17-20": 100,
                            "21-22": 175}
        self.decreasePts = {"16": 15,
                            "17-20": 10,
                            "21-22": 17}
        self.finBonus = {"16": [650, 585, 520, 455, 390, 325, 260, 195, 130, 65],
                         "17-20": [1050, 945, 840, 735, 630, 525, 420, 315, 210, 105],
                         "21-22": [375, 340, 305, 270, 235, 200, 165, 130, 95, 60]}

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, GR1, GR2, GR3, GR4, GR5, GR5, GR6, GR7, GR8, GRB FROM MCCDATA WHERE AR_PLACE IS NOT NULL AND PLAYER = player" + extra_query
        GameAbstract.calc(self, cur, player, scoring_type, query)
