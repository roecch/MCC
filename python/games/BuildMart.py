from python.constants import cur_latest_event
from python.games.GameAbstract import GameAbstract


class BuildMart:
    def __init__(self):
        self.scores = {"1-16": [140, 132, 124, 116, 108, 100, 92, 84, 76, 68],
                       "17-" + cur_latest_event: [128, 120, 112, 100, 88, 76, 64, 52, 36, 20]}

    @staticmethod
    def calcOneEvent(data, scores):
        total = 0
        for build in data:
            try:
                total += scores[int(float(build)) - 1]
            except IndexError:
                return 0
        return total

    def calcAuto(self, data):
        total = 0
        for event in data:
            num = event[0][3:]
            scoresPts = self.scores[GameAbstract.getKeyFromNum(self, num, self.scores.keys())]
            total += self.calcOneEvent(event[1:], scoresPts)
        return total

    def calcNew(self, data):
        total = 0
        scoresPts = self.scores[list(self.scores.keys())[len(self.scores.keys()) - 1]]
        for event in data:
            total += self.calcOneEvent(event[1:], scoresPts)
        return total

    def calcByOne(self, data, num: int):
        total = 0
        for event in data:
            scoresPts = self.scores[GameAbstract.getKeyFromNum(self, num, self.scores.keys())]
            total += self.calcOneEvent(event[1:], scoresPts)
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, BM FROM MCCDATA WHERE BM IS NOT NULL and PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
