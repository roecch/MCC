from python.games.KillsInterface import KillsInterface
from python.games.SurvivalInterface import SurvivalInterface


class Skyblockle(SurvivalInterface, KillsInterface):
    def __init__(self):
        self.surv = []
        self.kill = []

    def perKill(self) -> int:
        return 0

    def perSurvival(self) -> int:
        return 0

    def calc(self, cur, player: str, mccnum: str) -> int:
        return 0
