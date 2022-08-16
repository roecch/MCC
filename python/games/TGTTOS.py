from python.games.GameAbstract import GameAbstract
from python.games.RaceInterface import RaceInterface
from python.constants import cur_latest_event


class TGTTOS(RaceInterface):
    def __init__(self):
        self.placement = {"1-16": (80, 2),
                          "17": (40, 1, [60, 15]),
                          "18-" + cur_latest_event: (40, 1, [80, 5]),
                          }
        self.team_bonus = {"6-16": [100],
                           "17-" + cur_latest_event: [100, 75, 50, 25]}

    def calc_six_rounds(self, data, placementPts):
        total = 0
        for round_placem in data:
            if round_placem != "X":
                placem = int(float(round_placem))
                total += placementPts[0] - placementPts[1] * (40 - placem)
                if len(placementPts) > 2:
                    indiv_bonus = placementPts[2][0] - placementPts[2][1] * (placem - 1)
                    total += indiv_bonus if indiv_bonus > 0 else 0
        return total

    def calc_bonus(self, data, bonuses):
        total = 0

        if data is None:
            return 0

        data = data.split('-')
        for got_bonus in data:
            total += bonuses[got_bonus - 1]
        return total

    def calcAuto(self, data):
        total = 0
        for event in data:
            num = event[0][3:]
            placementPts = self.placement[GameAbstract.getKeyFromNum(self, num, self.placement.keys())]
            total = self.calc_six_rounds(event[1:7], placementPts)
            try:
                total += self.calc_bonus(event[7], self.team_bonus[GameAbstract.getKeyFromNum(self, num, self.team_bonus.keys())])
            except (ArithmeticError, TypeError) as e:
                pass
        return total

    def calcNew(self, data):
        total = 0
        placementPts = self.placementPts[list(self.placementPts.keys())[len(self.placementPts.keys()) - 1]]
        team_bonusPts = self.team_bonus[list(self.team_bonus.keys())[len(self.team_bonus.keys()) - 1]]
        for event in data:
            total = self.calc_six_rounds(event[1:7], placementPts[0], placementPts[1]) \
                    + self.calc_bonus(event[7], team_bonusPts)
        return total

    def calcByOne(self, data, num: int):
        total = 0
        for event in data:
            placementPts = self.placement[GameAbstract.getKeyFromNum(self, num, self.placement.keys())]
            total = self.calc_six_rounds(event[1:7], placementPts[0], placementPts[1]) \
                    + self.calc_bonus(event[7], self.team_bonus[GameAbstract.getKeyFromNum(self, num,
                                                                                           self.team_bonus.keys())])
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM,TGTTOS1,TGTTOS2,TGTTOS3,TGTTOS4,TGTTOS5,TGTTOS6,TGTTOS_BONUS " \
                "FROM MCCDATA WHERE TGTTOS1 IS NOT NULL and PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
