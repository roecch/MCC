from python.games.GameAbstract import GameAbstract
from python.games.KillsInterface import KillsInterface
from python.games.SurvivalInterface import SurvivalInterface
from python.constants import cur_latest_event


class SkyBattle(SurvivalInterface, KillsInterface):
    def __init__(self, cur):
        self.cur = cur
        self.survPts = {"9-" + cur_latest_event: (2, 50)}
        self.killPts = {"9-" + cur_latest_event: 50}

    def perSurvivalAndFinal(self, game, survPt, finalPt, mcc_num, team) -> int:
        total = 0
        for rnd in game:
            place = int(rnd)
            total += place * survPt
            query = "SELECT MAX(TEAM) FROM MCCDATA WHERE SB_KILLS IS NOT NULL AND MCCNUM = " + mcc_num + ";"
            self.cur.execute(query)
            last_team_standing = self.cur.fetchall()
            if team == last_team_standing:
                total += finalPt
        return total

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            survAndFinalpoints = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
            survPt = survAndFinalpoints[0]
            finalPt = survAndFinalpoints[1]
            total += self.perSurvivalAndFinal(game[2:], survPt, finalPt, num, game[1])
        return total

    def calcNew(self, data):
        total = 0
        survPt = self.survPts[list(self.survPts.keys())[len(self.survPts.keys()) - 1]]
        finalPt = self.topPts[list(self.topPts.keys())[len(self.topPts.keys()) - 1]]
        for game in data:
            total += self.perSurvivalAndFinal(game[2:], survPt, finalPt, game[0][3:], game[1])
        return total

    def calcByOne(self, data, num: int):
        total = 0
        survPt = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
        finalPt = self.topPts[GameAbstract.getKeyFromNum(self, num, self.topPts.keys())]
        for game in data:
            total += self.perSurvivalAndFinal(game[2:], survPt, finalPt, game[0][3:], game[1])
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, TEAM, SB_KILLS, SB_SURVIVAL1, SB_SURVIVAL2, SB_SURVIVAL3 " \
                "FROM MCCDATA WHERE SB_SURVIVAL1 IS NOT NULL AND PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
