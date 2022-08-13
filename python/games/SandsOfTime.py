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

    def get_divided(self, cur, player: str, extra_query: str):
        query = "SELECT SOT FROM MCCDATA WHERE SOT IS NOT NULL and PLAYER = player" + extra_query
        cur.execute(query.replace('player', "'" + player + "'"))
        data = cur.fetchall()
        total = 0
        for game in data:
            total += game[0]
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str):
        query = "SELECT SOT FROM MCCDATA WHERE SOT IS NOT NULL and PLAYER = player" + extra_query
        cur.execute(query.replace('player', "'" + player + "'"))
        data = cur.fetchall()
        total = 0
        for game in data:
            total += game[0]
        return total
