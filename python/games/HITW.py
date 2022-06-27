from python.games.GameAbstract import GameAbstract
from python.games.SurvivalInterface import SurvivalInterface


class HITW(SurvivalInterface):
    def __init__(self):
        self.survPts = {"1-22": 4}
        self.topPts = {"1-16": [200],
                       "17-22": [100, 70, 30]}

    def perSurvival(self, game, survPt, finalPt) -> int:
        total = 0
        for rnd in game:
            place = 40 - int(rnd)
            total += place * survPt
            try:
                total += finalPt[rnd - 1]
            except IndexError:
                pass
        return total

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            survPt = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
            finalPt = self.topPts[GameAbstract.getKeyFromNum(self, num, self.topPts.keys())]
            total += self.perSurvival(game[1:], survPt, finalPt)
        return total

    def calcNew(self, data):
        total = 0
        survPt = self.survPts[list(self.survPts.keys())[len(self.survPts.keys()) - 1]]
        finalPt = self.topPts[list(self.topPts.keys())[len(self.topPts.keys()) - 1]]
        for game in data:
            total += self.perSurvival(game, survPt, finalPt)
        return total

    def calcByOne(self, data, num: int):
        total = 0
        survPt = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
        finalPt = self.topPts[GameAbstract.getKeyFromNum(self, num, self.topPts.keys())]
        for game in data:
            total += self.perSurvival(game, survPt, finalPt)
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, HITW1, HITW2, HITW3 FROM MCCDATA WHERE HITW1 IS NOT NULL AND PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
