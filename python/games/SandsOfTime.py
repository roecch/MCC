from python.games.GameAbstract import GameAbstract
from python.games.RaceInterface import RaceInterface
from python.constants import cur_latest_event


class SandsOfTime:

    def get_undivided(self, cur, player: str, extra_query: str):
        query = "SELECT SOT FROM MCCDATA WHERE SOT IS NOT NULL and PLAYER = player" + extra_query
        cur.execute(query.replace('player', "'" + player + "'"))
        data = cur.fetchall()
        total = 0
        for game in data:
            total += game[0]
        return total

    def get_divided(self, data):
        values = set(map(lambda x: x[0], data))
        data = [[y[1] for y in data if y[0] == x] for x in values]
        print(data)
        total = 0
        for game in data:
            total += sum(game) / 4
        print(total)
        return int(total / len(data))

    def calc(self, cur, player: str, scoring_type: str, extra_query: str):
        query = "SELECT MCCNUM, SOT FROM MCCDATA WHERE SOT IS NOT NULL AND (MCCNUM, TEAM) in (SELECT MCCNUM, " \
                "TEAM FROM MCCDATA WHERE SOT IS NOT NULL AND PLAYER = player) " + extra_query
        rows_count = cur.execute(query.replace('player', "'" + player + "'"))
        data = cur.fetchall()
        if rows_count > 0:
            return self.get_divided(data)
        else:
            return 0
