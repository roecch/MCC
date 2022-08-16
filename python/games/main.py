import mysql.connector

from python.games.AceRace import AceRace
from python.games.BattleBox import BattleBox
from python.games.BingoButFast import BingoButFast
from python.games.GridRunners import GridRunners
from python.games.HITW import HITW
from python.games.ParkourTag import ParkourTag
from python.games.ParkourWarrior import ParkourWarrior
from python.games.RocketSpleefRush import RocketSpleefRush
from python.games.SurvivalGames import SurvivalGames
from python.games.TGTTOS import TGTTOS


def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Iamc00l!rsb897h4",
        database="MCC"
    )

    cur = mydb.cursor(buffered=True)

    # BattleBox.calc(BattleBox(), cur, "dream", "new")
    # HITW.calc(HITW(),cur,"dream","auto")
    # AceRace.calc(AceRace(),cur,"dream",11)
    # Rocket Spleef.calc(RocketSpleef(),cur,"dream","auto")
    # SurvivalGames.calc(SurvivalGames(),cur,"dream","auto")
    # GridRunners.calc(GridRunners(),cur,"dream","auto")
    # ParkourTag.calc(ParkourTag(cur),cur,"dream","auto")
    # ParkourTag.calc_runner_round(ParkourTag(cur), 14, 'Red', 'GREEN', 19)
    # TGTTOS.calc(TGTTOS(cur), cur, "dream", "auto")
    # ParkourWarrior.calc(ParkourWarrior(), cur, 'dream', 'auto')
    BingoButFast.calc(BingoButFast(), cur, 'dream', 'auto', ';')

    try:
        for x in cur:
            print(x)
    except Exception:
        pass

    mydb.commit()
    mydb.close()


if __name__ == "__main__":
    main()
