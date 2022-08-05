# from zope.interface import interfacemethod
from python.games.GameAbstract import GameAbstract


class GameInterface(GameAbstract):
    def getKeyFromNum(self, num: int, keys):
        pass

    # @interfacemethod
    def calc(self, cur, player: str, mccnum: str) -> int:
        pass
