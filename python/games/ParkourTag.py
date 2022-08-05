from python.games.GameAbstract import GameAbstract
from python.games.KillsInterface import KillsInterface
from python.games.SurvivalInterface import SurvivalInterface


class ParkourTag(SurvivalInterface, KillsInterface):
    def __init__(self, cur):
        self.cur = cur
        # mcc: pts every 10 sec, shared with runners if ONE person lasts 60
        self.survPts = {"12-13": (10, 30),
                        "14": (10, 10),
                        "15-22": (2, 20)}
        # mcc: pts for tagging one player (decreases), tag all
        # mcc 15 tag all stays same
        # mcc 16 tag all decreases
        self.killPts = {"12-14": (8, 0, 0),
                        "15": (6, 20, 0),
                        "16-22": (6, 42, 7)}
        # 12-14 only hunter
        # others all
        self.huntFaster = {"12-14": 25,
                           "15-22": 30}

    def calc_hunter_round(
            self,
            num: int,
            hunterTeam: str,
            runnerTeam: str,
            hunterData: str,
            killPt: (int, int),
            huntFaster: int,
    ) -> int:
        runners = self.get_runners(hunterTeam, num, runnerTeam)
        print(runners)
        huntingTotal = 0
        if len(runners) == 3:
            huntingTotal += killPt[1] - killPt[2] * int(runners[-1] / 10)
            if hunterData[-1] == 'T':
                huntingTotal += huntFaster

        for runner in runners:
            huntingTotal += killPt[0] - int(runner / 10)

        print(huntingTotal)
        return huntingTotal

    def calc_runner_round(
            self,
            num: int,
            hunterTeam: str,
            runnerTeam: str,
            runnerData: int,
            survPt: (int, int)
    ) -> int:
        runningTotal = survPt[1] if 60 in self.get_runners(hunterTeam, num, runnerTeam) else 0
        runningTotal += (survPt[0] * int(runnerData / 10))
        print(runningTotal)
        return runningTotal

    def get_runners(self, hunterTeam: str, num: int, runnerTeam: str):
        query = "SELECT PT_hunterTeam FROM mccdata WHERE MCCNUM = 'num' AND TEAM = 'runnerTeam'"
        query = query.replace("hunterTeam", hunterTeam).replace("num", "MCC" + str(num)).replace("runnerTeam",
                                                                                                 runnerTeam)
        self.cur.execute("".join(query))
        return sorted([int(i[0][1:]) for i in self.cur.fetchall() if "T" not in i[0]])

    def calcCompleteGame(self, num, team, dataOf10Rounds, survPt, killPt, huntFasterPt):
        total = 0
        colors = ["Red", "Orange", "Yellow", "Lime", "Green", "Cyan", "Aqua", "Blue", "Purple", "Pink"]
        for x in range(len(colors)):
            sing_round = dataOf10Rounds[x]
            print(sing_round)
            if sing_round is None:
                continue
            if sing_round[0] == "T":  # Hunter
                total += self.calc_hunter_round(num, team, colors[x], sing_round, killPt, huntFasterPt)
            elif sing_round[0] == "F":  # Runner
                total += self.calc_runner_round(num, colors[x], team, int(sing_round[1:]), survPt)
            else:
                raise Exception("PT Data Error")
        print(total)
        return total

    def calcAuto(self, data):
        total = 0
        for game in data:
            num = game[0][3:]
            survPt = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
            killPt = self.killPts[GameAbstract.getKeyFromNum(self, num, self.killPts.keys())]
            huntFasterPt = self.huntFaster[GameAbstract.getKeyFromNum(self, num, self.huntFaster.keys())]
            total += self.calcCompleteGame(num, game[1], game[2:], survPt, killPt, huntFasterPt)
        print(total)
        return total

    def calcNew(self, data):
        total = 0
        survPt = self.survPts[list(self.survPts.keys())[len(self.survPts.keys()) - 1]]
        killPt = self.killPts[list(self.killPts.keys())[len(self.killPts.keys()) - 1]]
        huntFasterPt = self.huntFaster[list(self.huntFaster.keys())[len(self.huntFaster.keys()) - 1]]
        for game in data:
            num = game[0][3:]
            total += self.calcCompleteGame(num, game[1], game[2:], survPt, killPt, huntFasterPt)
        print(total)
        return total

    def calcByOne(self, data, num: int):
        total = 0
        survPt = self.survPts[GameAbstract.getKeyFromNum(self, num, self.survPts.keys())]
        killPt = self.killPts[GameAbstract.getKeyFromNum(self, num, self.killPts.keys())]
        huntFasterPt = self.huntFaster[GameAbstract.getKeyFromNum(self, num, self.huntFaster.keys())]
        for game in data:
            num = game[0][3:]
            total += self.calcCompleteGame(num, game[1], game[2:], survPt, killPt, huntFasterPt)
        print(total)
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, TEAM, " \
                "PT_RED, PT_ORANGE, PT_YELLOW, PT_LIME, PT_GREEN, " \
                "PT_CYAN, PT_AQUA, PT_BLUE, PT_PURPLE, PT_PINK " \
                "FROM MCCDATA WHERE NOT (PT_RED IS NULL AND PT_ORANGE IS NULL) AND PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
