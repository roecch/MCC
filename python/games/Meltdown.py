from python.constants import cur_latest_event
from python.games.GameAbstract import GameAbstract
from python.games.KillsInterface import KillsInterface


class Meltdown(KillsInterface):
    def __init__(self):
        # change to make starting point and desc pts a tuple
        self.killsAndCrates = {"22-" + cur_latest_event: (25, 10)}
        self.bonus = {"22-" + cur_latest_event: [210, 190, 170, 150, 125, 100, 80, 60, 45, 30]}

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            total += self.killsAndCrates[GameAbstract.getKeyFromNum(self, num, self.killsAndCrates.keys())][0] * game[
                1] + \
                     self.killsAndCrates[GameAbstract.getKeyFromNum(self, num, self.killsAndCrates.keys())][1] * game[
                         2] + \
                     self.bonus[GameAbstract.getKeyFromNum(self, num, self.bonus.keys())][game[3] - 1]
        return total

    def calcNew(self, data):
        total = 0
        kiAndCr = self.killsAndCrates[list(self.killsAndCrates.keys())[len(self.killsAndCrates.keys()) - 1]]
        bonusPt = self.bonus[list(self.bonus.keys())[len(self.bonus.keys()) - 1]]

        for game in data:
            total += kiAndCr[0] * game[1] + kiAndCr[1] * game[2] + bonusPt[game[3] - 1]
        return total

    def calcByOne(self, data, num: int):
        total = 0
        kiAndCr = self.skillsAndCrates[GameAbstract.getKeyFromNum(self, num, self.killsAndCrates.keys())]
        bonusPt = self.bonus[GameAbstract.getKeyFromNum(self, num, self.bonus.keys())]

        for game in data:
            total += kiAndCr[0] * game[1] + kiAndCr[1] * game[2] + bonusPt[game[3] - 1]
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, MD_KILLS, MD_CRATES, MD_SURVIVAL FROM MCCDATA WHERE MD_KILLS IS NOT NULL and PLAYER = " \
                "player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
