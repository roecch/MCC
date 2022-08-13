from python.games.GameAbstract import GameAbstract


class LockoutBingo:
    def __init__(self):
        self.compPts = {"1-5": [45, 30, 20, 10, 5]}

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, LOCK_BINGO FROM MCCDATA WHERE LOCK_BINGO IS NOT NULL AND PLAYER = player" + extra_query
        cur.execute(query.replace('player', "'" + player + "'"))
        data = cur.fetchall()
        total = 0
        for game in data:
            total += game[0]
        return total
