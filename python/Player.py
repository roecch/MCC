import mysql.connector
import sys

from python.constants import cur_latest_event
from python.games.SkyBlockle import SkyBlockle
from python.games.AceRace import AceRace
from python.games.BattleBox import BattleBox
from python.games.BingoButFast import BingoButFast
from python.games.BuildMart import BuildMart
from python.games.FootRace import FootRace
from python.games.GridRunners import GridRunners
from python.games.HITW import HITW
from python.games.LockoutBingo import LockoutBingo
from python.games.Meltdown import Meltdown
from python.games.ParkourTag import ParkourTag
from python.games.ParkourWarrior import ParkourWarrior
from python.games.RocketSpleef import RocketSpleef
from python.games.RocketSpleefRush import RocketSpleefRush
from python.games.SandsOfTime import SandsOfTime
from python.games.SkyBattle import SkyBattle
from python.games.SurvivalGames import SurvivalGames
from python.games.TGTTOS import TGTTOS


class Player:
    def __init__(self, name, cursor):
        self.name = name
        self.cur = cursor

    # def cal_player_avg(self, scoring_type: str = 'auto', include_season_one: bool = True) -> int:
    #     ignore_events = []
    #     if not include_season_one:
    #         ignore_events = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    #     avg = 0
    #     num_of_included_events = 0
    #
    #     query = "SELECT MCCNUM FROM MCCDATA WHERE PLAYER = '" + self.name + "';"
    #     self.cur.execute(query)
    #     mccs = self.cur.fetchall()
    #     mccs = [i[0][3:] for i in mccs]
    #
    #     for x in [i for i in mccs if i not in ignore_events]:
    #         num_of_included_events += 1
    #         print(self.calc_some_events(str(" AND MCCNUM = 'MCC" + str(x) + "';"), scoring_type, True))
    #         avg += sum(self.calc_some_events(str(" AND MCCNUM = 'MCC" + str(x) + "';"), scoring_type, True))
    #     return int(avg / num_of_included_events)

    def cal_player_avg(self, scoring_type: str = 'auto', include_season_one: bool = True) -> float:
        ignore_events = []
        if not include_season_one:
            ignore_events = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        num_of_included_events = 0

        query = "SELECT EVENT_TOTAL FROM MCCDATA WHERE PLAYER = '" + self.name + "';"
        self.cur.execute(query)
        totals = self.cur.fetchall()
        totals = [i[0] for i in totals]
        return float(f'{(sum(totals) / len(totals)):.2f}')

    def calc_cur_games(self, scoring_type: str = 'auto', ignore_events: [] = []):
        extra_query = ";"
        if ignore_events:
            extra_query = " AND MCCNUM NOT IN " + str(map(lambda x: "MCC" + str(x), ignore_events)) + ";"
        return self.calc_some_events(extra_query, scoring_type, False)

    def calc_some_events(self, extra_query, scoring_type, if_all_games):
        list_of_scores = \
            [AceRace.calc(AceRace(), self.cur, self.name, scoring_type, extra_query),
             BattleBox.calc(BattleBox(), self.cur, self.name, scoring_type, extra_query),
             BuildMart.calc(BuildMart(), self.cur, self.name, scoring_type, extra_query),
             GridRunners.calc(GridRunners(), self.cur, self.name, scoring_type, extra_query),
             HITW.calc(HITW(), self.cur, self.name, scoring_type, extra_query),
             Meltdown.calc(Meltdown(), self.cur, self.name, scoring_type, extra_query),
             ParkourTag.calc(ParkourTag(self.cur), self.cur, self.name, scoring_type, extra_query),
             RocketSpleefRush.calc(RocketSpleefRush(), self.cur, self.name, scoring_type, extra_query),
             SandsOfTime.calc(SandsOfTime(), self.cur, self.name, scoring_type, extra_query),
             SkyBattle.calc(SkyBattle(self.cur), self.cur, self.name, scoring_type, extra_query),
             SurvivalGames.calc(SurvivalGames(self.cur), self.cur, self.name, scoring_type, extra_query),
             TGTTOS.calc(TGTTOS(), self.cur, self.name, scoring_type, extra_query),
             ]
        if if_all_games:
            more_scores = [
                # BingoButFast.calc(BingoButFast(), self.cur, self.name, scoring_type, extra_query),
                # FootRace.calc(FootRace(), self.cur, self.name, scoring_type, extra_query),
                # LockoutBingo.calc(LockoutBingo(), self.cur, self.name, scoring_type, extra_query),
                # ParkourWarrior.calc(ParkourWarrior(), self.cur, self.name, scoring_type, extra_query),
                # RocketSpleef.calc(RocketSpleef(), self.cur, self.name, scoring_type, extra_query),
                # SkyBlockle.calc(SkyBlockle(self.cur), self.cur, self.name, scoring_type, extra_query),
            ]
            list_of_scores += more_scores
        return list_of_scores

    def get_player(self):
        return


def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Iamc00l!rsb897h4",
    )

    cur = mydb.cursor(buffered=True)

    cur.execute("USE MCC;")
    cur.close()


if __name__ == "__main__":
    main()
