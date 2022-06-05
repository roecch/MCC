import csv
import pandas as pd

import mysql.connector

global all_players
all_players = ['5up', 'Antfrost', 'Asnazum', 'Awesamdude', 'BadBoyHalo', 'BBPaws', 'Bitzel', 'CaptainPuffy', 'CaptainSparklez', 'ConnorEatsPants',
               'Cubfan135', 'Calvin', 'DanTDM', 'DethRidge', 'Dream', 'DrGluon', 'ElainaExe', 'Eret', 'F1NN5TER', 'FalseSymmetry', 'FlorianFunke',
               'fruitberries', 'Fundy', 'fWhip', 'GeeNelly', 'GeminiTay', 'GeorgeNotFound', 'GizzyGazza', 'GoodTimesWithScar', 'Grian', 'Graser10',
               'HBomb94', 'iHasCupquake', 'iicbunny', 'iJevin', 'Illumina', 'InTheLittleWood', 'iskall85', 'ItsJustOriah', 'JackManifoldTV',
               'JackSucksAtLife', 'JamesCharles', 'Jameskii', 'JamesTurner', 'JcTheCaster', 'JeromeASF', 'Jestannii', 'JoeyGraceffa', 'jojosolos', 'KaraCorvus',
               'KarlJacobs', 'Katherineelizabeth', 'KingBurren', 'Kontuz', 'Krinios', 'Krtzyy', 'KryticZeuZ', 'Laurenzside', 'LDShadowLady', 'Ludwig',
               'Marielitai', 'Mefs', 'Michaelmcchill', 'MiniMuka', 'NettyPlays', 'Nihachu', 'PEARLBYTEZ', 'PearlescentMoon', 'PeteZahHuTt', 'Ph1LzA',
               'Plumbella', 'Pokimane', 'Ponk', 'PrestonPlayz', 'Punz', 'Purpled', 'Quackity', 'Quig', 'Rafessor', 'Ranboo', 'Rendog', 'RipMika',
               'Roguskii', 'RTGame', 'Ryguyrocky', 'Sapnap', 'SB737', 'ScotGriswold', 'Seapeekay', 'Shubble', 'Skeppy', 'Slimecicle', 'Smajor1995',
               'Smallishbeans', 'Sneegsnag', 'SolidarityGaming', 'Spifey', 'Steph0sims', 'Strawburry17', 'Sylvee', 'TankMatt', 'Tapl', 'Technoblade',
               'TheOrionSound', 'TommyInnit', 'ToxxxicSupport', 'Tubbo', 'Vapekit', 'vGumiho', 'Vikkstar', 'Vixella', 'VoiceoverPete', 'WilburSoot',
               'Wisp', 'Wolv21', 'Yammy', 'YeetDaisie']


def setNullTables(cur):
    # cur.execute("SELECT TABLE_NAME from information_schema.tables where TABLE_SCHEMA = 'mcc'")
    for player in all_players:
        createQuery = ['CREATE TABLE ', player, '(MCCNUM VARCHAR(20), TEAM VARCHAR(20), AR_TIME TIME NULL, AR_PLACE INT NULL, BB_KILLS '
                                                'INT NULL, BB_WINS INT NULL, BINGO VARCHAR(20) NULL, BM VARCHAR(20) NULL, FT_TIME TIME NULL, FT_PLACE INT '
                                                'NULL, GR1 INT NULL, GR2 INT NULL, GR3 INT NULL, GR4 INT NULL, GR5 INT NULL, GR6 INT NULL, GR7 INT NULL, '
                                                'GR8 INT NULL, GRB INT NULL, HITW1 INT NULL, '
                                                'HITW2 INT NULL, HITW3 INT NULL, PT_RED VARCHAR(20) NULL, PT_ORANGE VARCHAR(20) NULL, PT_YELLOW VARCHAR(20) '
                                                'NULL, PT_LIME VARCHAR(20) NULL, PT_GREEN VARCHAR(20) NULL, PT_CYAN VARCHAR(20) NULL, PT_AQUA VARCHAR(20) '
                                                'NULL, PT_BLUE VARCHAR(20) NULL, PT_PURPLE VARCHAR(20) NULL, PT_PINK VARCHAR(20) NULL, '
                                                'PW_COURSE VARCHAR(20) NULL, RS_KILLS INT NULL, RS1 INT NULL, RS2 INT NULL, RS3 INT NULL, SB_KILLS INT '
                                                'NULL, SB_SURVIVAL1 TIME NULL, SB_SURVIVAL2 TIME NULL, SB_SURVIVAL3 TIME NULL, SOT VARCHAR(20) NULL, '
                                                'SKYB_KILLS VARCHAR(20) NULL, SKYB_SURVIVAL VARCHAR(20) NULL, SG_KILLS INT NULL, SG_SURVIVAL INT NULL, '
                                                'TGTTOS1 VARCHAR(20) NULL, TGTTOS2 VARCHAR(20) NULL, TGTTOS3 VARCHAR( '
                                                '20), TGTTOS4 VARCHAR(20) NULL, TGTTOS5 VARCHAR(20) NULL, TGTTOS6 VARCHAR(20) NULL);']
        query = "".join(createQuery)
        cur.execute(query)


def drop_all(cur):
    cur.execute("SELECT TABLE_NAME from information_schema.tables where TABLE_SCHEMA = 'mcc'")
    data = cur.fetchall()
    for player in data:
        createQuery = ['DROP TABLE ', player[0], ';']
        query = "".join(createQuery)
        cur.execute(query)


def set_single_MCC_data(cur, rowStart, rowEnd, colStart, colEnd):
    df = pd.read_csv('../data/MCCFull.csv', header=0, index_col=0)
    df = df.iloc[rowStart:rowEnd, colStart:colEnd]
    print(df)
    header = df.head(0).columns
    print(header)
    NumAndGames = []
    for game in header:
        # header glitches and puts trailing decimals after each game
        try:
            game = game[0:game.index('.')]
        except Exception:
            pass
        if game[0:3] == "MCC":
            NumAndGames.append("MCCNUM")
        elif game == "Team":
            NumAndGames.append("TEAM")
        elif game == "Ace Race - Time":
            NumAndGames.append("AR_TIME")
        elif game == "Ace Race - Place":
            NumAndGames.append("AR_PLACE")
        elif game == "Battle Box - Kills":
            NumAndGames.append("BB_KILLS")
        elif game == "Battle Box - Wins":
            NumAndGames.append("BB_WINS")
        elif game == "Bingo But Fast" or game == "Lockout Bingo":
            NumAndGames.append("BINGO")
        elif game == "Build Mart":
            NumAndGames.append("BM")
        elif game == "Foot Race - Time":
            NumAndGames.append("FT_TIME")
        elif game == "Foot Race - Place":
            NumAndGames.append("FT_PLACE")
        elif game == "Grid Runners - 1":
            NumAndGames.append("GR1")
        elif game == "Grid Runners - 2":
            NumAndGames.append("GR2")
        elif game == "Grid Runners - 3":
            NumAndGames.append("GR3")
        elif game == "Grid Runners - 4":
            NumAndGames.append("GR4")
        elif game == "Grid Runners - 5":
            NumAndGames.append("GR5")
        elif game == "Grid Runners - 6":
            NumAndGames.append("GR6")
        elif game == "Grid Runners - 7":
            NumAndGames.append("GR7")
        elif game == "Grid Runners - 8":
            NumAndGames.append("GR8")
        elif game == "Grid Runners - Bonus":
            NumAndGames.append("GRB")
        elif game == "Hole in the Wall - 1":
            NumAndGames.append("HITW1")
        elif game == "Hole in the Wall - 2":
            NumAndGames.append("HITW2")
        elif game == "Hole in the Wall - 3":
            NumAndGames.append("HITW3")
        elif game == "Parkour Tag - Red":
            NumAndGames.append("PT_RED")
        elif game == "Parkour Tag - Orange":
            NumAndGames.append("PT_ORANGE")
        elif game == "Parkour Tag - Yellow":
            NumAndGames.append("PT_YELLOW")
        elif game == "Parkour Tag - Lime":
            NumAndGames.append("PT_LIME")
        elif game == "Parkour Tag - Green":
            NumAndGames.append("PT_GREEN")
        elif game == "Parkour Tag - Cyan":
            NumAndGames.append("PT_CYAN")
        elif game == "Parkour Tag - Aqua":
            NumAndGames.append("PT_AQUA")
        elif game == "Parkour Tag - Blue":
            NumAndGames.append("PT_BLUE")
        elif game == "Parkour Tag - Purple":
            NumAndGames.append("PT_PURPLE")
        elif game == "Parkour Tag - Pink":
            NumAndGames.append("PT_PINK")
        elif game == "Parkour Warrior - Course":
            NumAndGames.append("PW_COURSE")
        elif game == "Rocket Spleef - Kills":
            NumAndGames.append("RS_KILLS")
        elif game == "Rocket Spleef - 1":
            NumAndGames.append("RS1")
        elif game == "Rocket Spleef - 2":
            NumAndGames.append("RS2")
        elif game == "Rocket Spleef - 3":
            NumAndGames.append("RS3")
        elif game == "Sky Battle - Kills":
            NumAndGames.append("SB_KILLS")
        elif game == "Sky Battle - 1":
            NumAndGames.append("SB_SURVIVAL1")
        elif game == "Sky Battle - 2":
            NumAndGames.append("SB_SURVIVAL2")
        elif game == "Sky Battle - 3":
            NumAndGames.append("SB_SURVIVAL3")
        elif game == "Sands Of Time":
            NumAndGames.append("SOT")
        elif game == "Skyblockle - Kills":
            NumAndGames.append("SKYB_KILLS")
        elif game == "Skyblockle - Survival":
            NumAndGames.append("SKYB_SURVIVAL")
        elif game == "SG - Kills":
            NumAndGames.append("SG_KILLS")
        elif game == "SG - Survival":
            NumAndGames.append("SG_SURVIVAL")
        elif game == "TGTTOS1":
            NumAndGames.append("TGTTOS1")
        elif game == "TGTTOS2":
            NumAndGames.append("TGTTOS2")
        elif game == "TGTTOS3":
            NumAndGames.append("TGTTOS3")
        elif game == "TGTTOS4":
            NumAndGames.append("TGTTOS4")
        elif game == "TGTTOS5":
            NumAndGames.append("TGTTOS5")
        elif game == "TGTTOS6":
            NumAndGames.append("TGTTOS6")
    print(len(NumAndGames))

    players = list(df.index.values)
    for i, row in enumerate(df.to_numpy()):
        row = list(row)
        print(len(row))
        row.pop(0)
        createQuery = ['INSERT INTO ', players[i], ' (', ', '.join(NumAndGames), ') Values (', "'", header[0], "'", ',%s)']
        query = "".join(createQuery) % ','.join('?' * len(row))
        print(check_sql_string(query, row).replace("nan", "NULL"))
        cur.execute(check_sql_string(query, row).replace("nan", "NULL"))


def setAllMCCData(cur):
    with open('../data/MCCFull.csv') as f:
        reader = csv.reader(f, delimiter=",")
        games = next(reader)
        players = [row[0] for row in reader]
        players.insert(0, games.pop(0))

    res = [i for i in games if 'MCC' in i]
    for x in range(len(res)):
        if x != len(res) - 1:
            set_single_MCC_data(cur, players.index(res[x]), int(players.index(res[x + 1]) - 1),
                                games.index(res[x]), int(games.index(res[x + 1])))
        else:
            set_single_MCC_data(cur, players.index(res[x]), len(players),
                                games.index(res[x]), len(games))


def check_sql_string(sql, values):
    unique = "%PARAMETER%"
    sql = sql.replace("?", unique)
    for v in values:
        sql = sql.replace(unique, repr(v), 1)
    return sql


def main():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Iamc00l!rsb897h4",
        database="MCC"
    )

    cur = mydb.cursor(buffered=True)

    drop_all(cur)
    setNullTables(cur)
    setAllMCCData(cur)

    try:
        for x in cur:
            print(x)
    except Exception:
        pass

    mydb.commit()
    mydb.close()


if __name__ == "__main__":
    main()
