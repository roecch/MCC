from python.games.GameAbstract import GameAbstract


class BingoButFast:
    def __init__(self):
        # self.compPts = {"6-13": [45, 30, 20, 10, 5]}
        self.compPts = [45, 30, 20, 10, 5]

    def calc_round(self, data):
        total = 0
        data = data.split('-')
        for i in range(5):
            total += int(data[i]) * self.compPts[i]
        return total

    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, TEAM, BINGO_FAST FROM MCCDATA WHERE BINGO_FAST IS NOT NULL AND (MCCNUM, TEAM) in (" \
                "SELECT MCCNUM, TEAM FROM MCCDATA WHERE BINGO_FAST IS NOT NULL AND PLAYER = player)" + \
                extra_query
        rows_count = cur.execute(query.replace('player', "'" + player + "'"))
        data = cur.fetchall()
        print(data)
        if rows_count > 0:
            total = 0
            s = set([x[0] for x in data])
            print(s)
            for game in data:
                print(game)
                total += self.calc_round(game[2])
            print(total)
            return int(total / len(data))
        else:
            return 0
