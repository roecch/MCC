from python.games.GameAbstract import GameAbstract
from python.games.KillsInterface import KillsInterface
from python.games.SurvivalInterface import SurvivalInterface
from python.constants import cur_latest_event


class RocketSpleefRush(SurvivalInterface, KillsInterface):
    def __init__(self):
        self.survPts = {"1-19": (4, [100]),
                        "20-" + cur_latest_event: (3, [150, 125, 110, 100, 90, 85, 80, 75, 70, 65])}
        self.killPts = {"20-" + cur_latest_event: 10}

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
            killPt = self.killPts[GameAbstract.getKeyFromNum(self, num, self.killPts.keys())]
            total += self.perSurvival(game[2:], survPt[0], survPt[1]) + (game[1] * killPt)
        return total

    def calcNew(self, data):
        total = 0
        survPt = self.survPts[list(self.survPts.keys())[len(self.survPts.keys()) - 1]]
        killPt = self.killPts[list(self.killPts.keys())[len(self.killPts.keys()) - 1]]
        for game in data:
            total += self.perSurvival(game[2:], survPt[0], survPt[1]) + (game[1] * killPt)
        return total

    def calcByOne(self, data, num: int):
        total = 0
        survPt = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
        killPt = self.killPts[GameAbstract.getKeyFromNum(self, num, self.killPts.keys())]
        for game in data:
            total += self.perSurvival(game[2:], survPt[0], survPt[1]) + (game[1] * killPt)
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, RSR_KILLS, RSR1, RSR2, RSR3 FROM MCCDATA WHERE RSR1 IS NOT NULL AND PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
