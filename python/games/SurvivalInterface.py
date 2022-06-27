from zope.interface import interfacemethod

from python.games.GameInterface import GameInterface


class SurvivalInterface(GameInterface):
    @interfacemethod
    def perSurvival(self):
        pass
