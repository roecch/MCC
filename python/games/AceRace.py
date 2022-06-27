from python.games.GameAbstract import GameAbstract
from python.games.RaceInterface import RaceInterface


class AceRace(RaceInterface):
    def __init__(self):
        # change to make starting point and desc pts a tuple
        self.startingPts = {"7-14": 500,
                            "15-22": 400}
        self.decreasePts = {"7-14": 12.5,
                            "15-22": 10.0}
        self.bonus = {"7-14": [],
                      "15": [400, 250, 175, 100, 50, 25],
                      "16-22": [300, 240, 180, 120, 60, 15]}

    def placementPts(self, strtPt, decsPt, bonPt, placement) -> int:
        total = 0
        total += (strtPt - decsPt * (placement - 1))
        try:
            total += bonPt[placement - 1]
        except IndexError:
            pass
        print(total)
        return total

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            total += self.placementPts(self.startingPts[GameAbstract.getKeyFromNum(self, num, self.startingPts.keys())]
                                       , self.decreasePts[GameAbstract.getKeyFromNum(self, num, self.decreasePts.keys())]
                                       , self.bonus[GameAbstract.getKeyFromNum(self, num, self.bonus.keys())], game[1])
        return total

    def calcNew(self, data):
        total = 0
        startingPt = self.startingPts[list(self.startingPts.keys())[len(self.startingPts.keys()) - 1]]
        decreasePt = self.decreasePts[list(self.decreasePts.keys())[len(self.decreasePts.keys()) - 1]]
        bonusPt = self.bonus[list(self.bonus.keys())[len(self.bonus.keys()) - 1]]

        for game in data:
            self.placementPts(startingPt, decreasePt, bonusPt, game[1])
        return total

    def calcByOne(self, data, num: int):
        total = 0
        startingPt = self.startingPts[GameAbstract.getKeyFromNum(self, num, self.startingPts.keys())]
        decreasePt = self.decreasePts[GameAbstract.getKeyFromNum(self, num, self.decreasePts.keys())]
        bonusPt = self.bonus[GameAbstract.getKeyFromNum(self, num, self.bonus.keys())]

        for game in data:
            self.placementPts(startingPt, decreasePt, bonusPt, game[1])
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, AR_PLACE FROM MCCDATA WHERE AR_PLACE IS NOT NULL and PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
