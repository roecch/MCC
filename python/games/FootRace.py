from python.games.GameAbstract import GameAbstract
from python.games.RaceInterface import RaceInterface
from python.constants import cur_latest_event


class FootRace(RaceInterface):
    def __init__(self):
        # change to make starting point and desc pts a tuple
        self.startingPts = {"1-6": 500}
        self.decreasePts = {"1-6": 12.5}

    def placementPts(self, strtPt, decsPt, placement) -> int:
        total = 0
        total += (strtPt - decsPt * (placement - 1))
        return total

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            total += self.placementPts(self.startingPts[GameAbstract.getKeyFromNum(self, num, self.startingPts.keys())],
                                       self.decreasePts[GameAbstract.getKeyFromNum(self, num, self.decreasePts.keys())],
                                       game[1])
        return total

    def calcNew(self, data):
        total = 0
        startingPt = self.startingPts[list(self.startingPts.keys())[len(self.startingPts.keys()) - 1]]
        decreasePt = self.decreasePts[list(self.decreasePts.keys())[len(self.decreasePts.keys()) - 1]]

        for game in data:
            self.placementPts(startingPt, decreasePt, game[1])
        return total

    def calcByOne(self, data, num: int):
        total = 0
        startingPt = self.startingPts[GameAbstract.getKeyFromNum(self, num, self.startingPts.keys())]
        decreasePt = self.decreasePts[GameAbstract.getKeyFromNum(self, num, self.decreasePts.keys())]

        for game in data:
            self.placementPts(startingPt, decreasePt, game[1])
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, FR_PLACE FROM MCCDATA WHERE FR_PLACE IS NOT NULL and PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
