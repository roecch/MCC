from python.games.GameAbstract import GameAbstract
from python.games.RaceInterface import RaceInterface


class TGTTOS(RaceInterface):
    def __init__(self, cur):
        self.placement = {"1-14": (100, 5),
                          "15-23": (150, 10)}
        self.team_bonus = {"1-14": [30],
                           "15-23": [90, 70, 50, 30]}

    def calc_six_rounds(self, data, strtPt, decsPt):
        total = 0
        for round_placem in data:
            if round_placem != "X":
                total += (strtPt - decsPt * (round_placem - 1))
        return total

    def calc_bonus(self, data, bonuses):
        total = 0
        for got_bonus in data:
            total += bonuses[got_bonus - 1]
        return total

    def calcAuto(self, data):
        total = 0
        for event in data:
            num = event[0][3:]
            placementPts = self.placement[GameAbstract.getKeyFromNum(self, num, self.placement.keys())]
            total = self.calc_six_rounds(event[1:7], placementPts[0], placementPts[1]) \
                    + self.calc_bonus(event[7], self.team_bonus[GameAbstract.getKeyFromNum(self, num, self.team_bonus.keys())])
        return total

    def calcNew(self, data):
        total = 0

    def calcByOne(self, data, num: int):
        total = 0

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM,TGTTOS1,TGTTOS2,TGTTOS3,TGTTOS4,TGTTOS5,TGTTOS6 " \
                "FROM MCCDATA WHERE TGTTOS1 IS NOT NULL and PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
