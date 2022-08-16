from python.games.GameAbstract import GameAbstract
from python.games.KillsInterface import KillsInterface
from python.games.SurvivalInterface import SurvivalInterface
from python.constants import cur_latest_event, team_colors


class SurvivalGames(SurvivalInterface, KillsInterface):
    def __init__(self, cur):
        self.cur = cur
        self.surv = {"1-9": (10, [150]),
                     "10-14": (8, [150]),
                     "15-16": (8, [100]),
                     "17": (5, [650, 610, 570, 530, 490, 450, 410, 370, 330, 290]),
                     "18": (5, [750, 700, 660, 620, 580, 540, 500, 460, 420, 380]),
                     "19-" + cur_latest_event: (3, [650, 600, 560, 520, 480, 450, 420, 390, 360, 330])}
        self.kill = {"1-3": 50,
                     "4-9": 60,
                     "10-16": 100,
                     "17-18": 35,
                     "19-" + cur_latest_event: 65}
        self.drops = {"18": 200,
                      "19-" + cur_latest_event: 180}

    # final placement of team survival
    def finalDeath(self, team_color, survPts, mcc_num):
        colors = team_colors.copy()
        query = "SELECT SG_SURVIVAL FROM MCCDATA WHERE MCCNUM = 'MCC" + mcc_num + "' ORDER BY SG_SURVIVAL desc limit " \
                                                                                  "0,1; "
        self.cur.execute(query)
        highest_placement = self.cur.fetchall()[0][0]
        placement = 0

        for x in range(highest_placement, 0, -1):
            query = "SELECT TEAM FROM MCCDATA WHERE MCCNUM = 'MCC" + mcc_num + "' AND SG_SURVIVAL = " + str(x) + ";"
            self.cur.execute(query)
            team = self.cur.fetchall()[0][0]
            if team_color == team:
                try:
                    return survPts[placement]
                except IndexError:
                    return 0
            elif team in colors:
                placement += 1
                colors.remove(team)

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            survPt = self.surv[GameAbstract.getKeyFromNum(self, num, self.surv.keys())]
            killPt = self.kill[GameAbstract.getKeyFromNum(self, num, self.kill.keys())]
            total += game[3] * survPt[0] + self.finalDeath(game[1], survPt[1], num) + game[2] * killPt
            try:
                total += game[4] * self.drops[GameAbstract.getKeyFromNum(self, num, self.drops.keys())]
            except (ArithmeticError, TypeError) as e:
                pass
        return total

    def calcNew(self, data):
        total = 0
        survPt = self.surv[list(self.surv.keys())[len(self.surv.keys()) - 1]]
        killPt = self.kill[list(self.kill.keys())[len(self.kill.keys()) - 1]]
        for game in data:
            total += game[3] * survPt[0] + self.finalDeath(game[1], survPt[1], game[0][3:]) + game[2] * killPt
            try:
                total += game[4] * self.drops[list(self.drops.keys())[len(self.drops.keys()) - 1]]
            except (ArithmeticError, TypeError) as e:
                pass
        return total

    def calcByOne(self, data, num: int):
        total = 0
        survPt = self.surv[GameAbstract.getKeyFromNum(self, num, self.surv.keys())]
        killPt = self.kill[GameAbstract.getKeyFromNum(self, num, self.kill.keys())]
        for game in data:
            total += game[3] * survPt[0] + self.finalDeath(game[1], survPt[1], game[0][3:]) + game[2] * killPt
            try:
                total += game[4] * self.drops[GameAbstract.getKeyFromNum(self, num, self.drops.keys())]
            except (ArithmeticError, TypeError) as e:
                pass
        return total

    # mccnum -> mcc to calculate by
    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, TEAM, SG_KILLS, SG_SURVIVAL, SG_CRATES FROM MCCDATA WHERE SG_KILLS IS NOT NULL AND " \
                "PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
