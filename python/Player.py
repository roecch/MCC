import mysql.connector
import sys

from python.games.AceRace import AceRace
from python.games.BattleBox import BattleBox
from python.games.BuildMart import BuildMart
from python.games.FootRace import FootRace
from python.games.GridRunners import GridRunners
from python.games.HITW import HITW
from python.games.ParkourTag import ParkourTag
from python.games.RocketSpleef import RocketSpleef
from python.games.SkyBattle import SkyBattle
from python.games.Skyblockle import Skyblockle
from python.games.SurvivalGames import SurvivalGames
from python.games.TGTTOS import TGTTOS


class Player:
    def __init__(self, name, cur):
        self.name = name
        self.cur = cur

    @staticmethod
    def cal_player_avg(self, include_season_one: bool = true) -> int:
        ignore_events = []
        if not include_season_one:
            ignore_events = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        return 0

    def calc_all_games(self, cur, scoring_type, ignore_events: []):
        extra_query = ";"
        if ignore_events:
            extra_query = " AND MCCNUM NOT IN " + map(lambda x: "MCC" + str(x), ignore_events) + ";"
        list_of_scores = \
            [AceRace.calc(AceRace(), cur, self.name, scoring_type, extra_query),
             BattleBox.calc(BattleBox(), cur, self.name, scoring_type, extra_query),
             # BuildMart.calc(BuildMart(), cur, self.name, scoring_type, extra_query),
             FootRace.calc(FootRace(), cur, self.name, scoring_type, extra_query),
             # GridRunners.calc(GridRunners(), cur, self.name, scoring_type, extra_query),
             HITW.calc(HITW(), cur, self.name, scoring_type, extra_query),
             ParkourTag.calc(ParkourTag(cur), cur, self.name, scoring_type, extra_query),
             RocketSpleef.calc(RocketSpleef(), cur, self.name, scoring_type, extra_query),
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
    player = Player("dream", cur)
    print(Player.calc_all_games(Player("dream"), cur, "auto", []))


if __name__ == "__main__":
    main()
