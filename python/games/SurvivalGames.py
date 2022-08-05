from python.games.GameAbstract import GameAbstract
from python.games.KillsInterface import KillsInterface
from python.games.SurvivalInterface import SurvivalInterface
from python.constants import

class SurvivalGames(SurvivalInterface, KillsInterface):
    def __init__(self):
        last_key = '19-' cur_latest_event
        self.surv = {"1-9": (10, [150]),
                     "10-14": (8, [150]),
                     "15-16": (8, [100]),
                     "17": (5, [650, 610, 570, 530, 490, 450, 410, 370, 330, 290]),
                     "18": (5, [750, 700, 660, 620, 580, 540, 500, 460, 420, 380]),
                     last_key: (3, [650, 600, 560, 520, 480, 450, 420, 390, 360, 330])}
        self.kill = {"1-3": 50,
                     "4-9": 60,
                     "10-16": 100,
                     "17-18": 35,
                     "19-22": 65}
        self.drops = {"18": 200,
                      "19-22": 180}

    def perKill(self) -> int:
        return 0

    def perSurvival(self) -> int:
        return 0

    # mccnum -> mcc to calculate by
    def calc(self, cur, player: str, scoring_type: str, extra_query: str) -> int:
        query = "SELECT MCCNUM, SG_KILLS, SG_SURVIVAL FROM MCCDATA WHERE SG_KILLS IS NOT NULL AND PLAYER = player" + extra_query
        return GameAbstract.calc(self, cur, player, scoring_type, query)
