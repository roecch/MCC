from python.games.GameAbstract import GameAbstract
from python.games.KillsInterface import KillsInterface
from python.games.SurvivalInterface import SurvivalInterface


class SkyBattle(SurvivalInterface, KillsInterface):
    def __init__(self):
        self.survPts = {"9-22": (2, 50)}
        self.killPts = {"9-22": 50}

    def perSurvival(self, game, survPt, finalPt) -> int:
        total = 0
        for rnd in game:
            place = int(rnd)
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
            survAndFinalpoints = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
            survPt = survAndFinalpoints[0]
            finalPt = survAndFinalpoints[1]
            total += self.perSurvival(game[1:], survPt, finalPt)

    def calcNew(self, data):
        total = 0
        survPt = self.survPts[list(self.survPts.keys())[len(self.survPts.keys()) - 1]]
        finalPt = self.topPts[list(self.topPts.keys())[len(self.topPts.keys()) - 1]]
        for game in data:
            total += self.perSurvival(game, survPt, finalPt)

    def calcByOne(self, data, num: int):
        total = 0
        survPt = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
        finalPt = self.topPts[GameAbstract.getKeyFromNum(self, num, self.topPts.keys())]
        for game in data:
            total += self.perSurvival(game, survPt, finalPt)

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, SB_KILLS, SB_SURVIVAL1, SB_SURVIVAL2, SB_SURVIVAL3 " \
                "FROM MCCDATA WHERE SB_KILLS IS NOT NULL AND PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
