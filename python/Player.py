import mysql.connector
import sys

from python.games.AceRace import AceRace
from python.games.BattleBox import BattleBox
from python.games.BuildMart import BuildMart
from python.games.GridRunners import GridRunners
from python.games.HITW import HITW
from python.games.ParkourTag import ParkourTag
from python.games.RocketSpleef import RocketSpleef
from python.games.SkyBattle import SkyBattle
from python.games.Skyblockle import Skyblockle
from python.games.SurvivalGames import SurvivalGames
from python.games.TGTTOS import TGTTOS


class Player:
    def __init__(self, name, cursor):
        #
        # mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="Iamc00l!rsb897h4",
        # )
        #
        # cur = mydb.cursor(buffered=True)

        self.name = name
        self.cur = cursor

    def cal_player_avg(self, scoring_type: str = 'auto', include_season_one: bool = True) -> int:
        ignore_events = []
        if not include_season_one:
            ignore_events = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        avg = 0
        num_of_included_events = 0
        for x in range(0, 23) not in ignore_events:
            num_of_included_events += 1
            avg += self.calc_some_games(self, str(" AND MCCNUM = " + x + ";"), scoring_type)
        return int(avg / num_of_included_events)

    def calc_all_games(self, scoring_type: str = 'auto', ignore_events: [] = []):
        extra_query = ";"
        if ignore_events:
            extra_query = " AND MCCNUM NOT IN " + str(map(lambda x: "MCC" + str(x), ignore_events)) + ";"
        return self.calc_some_games(self, extra_query, scoring_type)

    def calc_some_games(self, extra_query, scoring_type):
        list_of_scores = \
            [AceRace.calc(AceRace(), self.cur, self.name, scoring_type, extra_query),
             BattleBox.calc(BattleBox(), self.cur, self.name, scoring_type, extra_query),
             # BuildMart.calc(BuildMart(), cur, self.name, scoring_type, extra_query),
             # GridRunners.calc(GridRunners(), cur, self.name, scoring_type, extra_query),
             HITW.calc(HITW(), self.cur, self.name, scoring_type, extra_query),
             ParkourTag.calc(ParkourTag(self.cur), self.cur, self.name, scoring_type, extra_query),
             RocketSpleef.calc(RocketSpleef(), self.cur, self.name, scoring_type, extra_query),
             # SkyBattle.calc(SkyBattle(), cur, self.name, scoring_type, extra_query),
             # Skyblockle.calc(Skyblockle(), cur, self.name, scoring_type, extra_query),
             # SurvivalGames.calc(SurvivalGames(), cur, self.name, scoring_type, extra_query),
             # TGTTOS.calc(TGTTOS(), cur, self.name, scoring_type, extra_query),
             ]
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
    print(Player.calc_all_games(Player("dream"), "auto", []))

    cur.close()


if __name__ == "__main__":
    main()
