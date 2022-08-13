from python.games.GameAbstract import GameAbstract
from python.games.RaceInterface import RaceInterface
from python.constants import cur_latest_event


class ParkourWarrior(RaceInterface):
    def __init__(self):
        # change to make starting point and desc pts a tuple
        self.section = {"1-11": (15, 20)}
        self.comp = {"1": 0,
                     "2": 740,
                     "3-6": 480,
                     "7-11": 280}

    def placementPts(self, stage, section, comp):
        sec = int(stage[1])
        sta = int(stage[0])
        fin = comp if int(sta) >= 9 else 0
        print(isinstance(section[0], str))
        print(isinstance(stage[0], str))
        print(isinstance(stage[1], str))
        print(isinstance(section[1], str))
        return section[0] * (sta * 3 + sec) + section[1] * sta + fin

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            stage = game[1].split('-') if '-' in game[1] else [9, 0]
            total += self.placementPts(stage, self.section[GameAbstract.getKeyFromNum(self, num, self.section.keys())],
                                       self.comp[GameAbstract.getKeyFromNum(self, num, self.comp.keys())])
        return total

    def calcNew(self, data):
        total = 0
        section = self.section[list(self.section.keys())[len(self.section.keys()) - 1]]
        comp = self.comp[list(self.comp.keys())[len(self.comp.keys()) - 1]]

        for game in data:
            stage = game[1].split('-') if '-' in game[1] else [9, 0]
            total += self.placementPts(stage, section, comp)
        return total

    def calcByOne(self, data, num: int):
        total = 0
        section = self.section[GameAbstract.getKeyFromNum(self, num, self.section.keys())]
        comp = self.comp[GameAbstract.getKeyFromNum(self, num, self.comp.keys())]

        for game in data:
            stage = game[1].split('-') if '-' in game[1] else [9, 0]
            total += self.placementPts(stage, section, comp)
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, PW_COURSE FROM MCCDATA WHERE PW_COURSE IS NOT NULL and PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
