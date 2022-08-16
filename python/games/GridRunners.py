from python.games.GameInterface import GameInterface
from python.games.GameAbstract import GameAbstract
from python.constants import cur_latest_event


class GridRunners(GameInterface):
    def __init__(self):
        self.starting = {"16": (150, 15),
                         "17-20": (100, 10),
                         "21-" + cur_latest_event: (175, 17)}
        self.finBonus = {"16": (650, 65),
                         "17-20": (1050, 105),
                         "21-" + cur_latest_event: (375, 35)}

    @staticmethod
    def calcRounds(data, strtPts):
        total = 0
        for room in data.split("-"):
            total += strtPts[0] - strtPts[1] * (int(float(room)) - 1)
        return total

    @staticmethod
    def calcBonus(data, fbPts):
        return fbPts[0] - fbPts[1] * (int(float(data)) - 1)

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            total += self.calcRounds(game[1],
                                     self.starting[GameAbstract.getKeyFromNum(self, num, self.starting.keys())]) + \
                     self.calcBonus(game[-1],
                                    self.finBonus[GameAbstract.getKeyFromNum(self, num, self.finBonus.keys())])
        return total

    def calcNew(self, data):
        total = 0
        startingPts = self.starting[list(self.starting.keys())[len(self.starting.keys()) - 1]]
        finBonusPts = self.finBonus[list(self.finBonus.keys())[len(self.finBonus.keys()) - 1]]
        for game in data:
            total += self.calcRounds(game[1], startingPts) + self.calcBonus(game[-1], finBonusPts)
        return total

    def calcByOne(self, data, num: int):
        total = 0
        startingPts = self.starting[GameAbstract.getKeyFromNum(self, num, self.starting.keys())]
        finBonusPts = self.finBonus[GameAbstract.getKeyFromNum(self, num, self.finBonus.keys())]
        for game in data:
            total += self.calcRounds(game[1], startingPts) + self.calcBonus(game[-1], finBonusPts)
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, GR, GRB FROM MCCDATA WHERE GR IS NOT NULL AND PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
