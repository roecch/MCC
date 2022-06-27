from python.games.RaceInterface import RaceInterface


class FootRace(RaceInterface):
    def __init__(self):
        self.place = []

    def placementPts(self) -> int:
        return 0
