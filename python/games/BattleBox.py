from python.games.GameAbstract import GameAbstract
from python.games.KillsInterface import KillsInterface
from python.constants import cur_latest_event


class BattleBox(KillsInterface):
    def __init__(self):
        self.killPts = {"1-" + cur_latest_event: 15}
        self.winPts = {"1-" + cur_latest_event: 160}

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            total += (game[2] * self.winPts[GameAbstract.getKeyFromNum(self, num, self.winPts.keys())]) + (game[1] * self.killPts[GameAbstract.getKeyFromNum(self, num, self.killPts.keys())])
        return total

    def calcNew(self, data):
        total = 0
        for game in data:
            total += (game[2] * self.winPts[list(self.winPts.keys())[len(self.winPts.keys()) - 1]]) + (game[1] * self.killPts[list(self.killPts.keys())[len(self.killPts.keys()) - 1]])
        return total

    def calcByOne(self, data, num: int):
        total = 0
        for game in data:
            total += (game[2] * self.winPts[GameAbstract.getKeyFromNum(self, num, self.winPts.keys())]) + (game[1] * self.killPts[GameAbstract.getKeyFromNum(self, num, self.killPts.keys())])
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, BB_KILLS, BB_WINS FROM MCCDATA WHERE BB_KILLS IS NOT NULL AND PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
