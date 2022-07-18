import csv
import pandas as pd

import mysql.connector


def create_table(cur):
    cur.execute('DROP TABLE IF EXISTS MCCDATA')
    createQuery = ['CREATE TABLE IF NOT EXISTS MCCDATA (MCCNUM VARCHAR(20), PLAYER VARCHAR(20), TEAM VARCHAR(20), AR_TIME TIME NULL, AR_PLACE INT NULL'
                   ', BB_KILLS INT NULL, BB_WINS INT NULL, BINGO_FAST VARCHAR(20) NULL, LOCK_BINGO VARCHAR(20) NULL, BM VARCHAR(20) NULL, FR_TIME TIME '
                   'NULL, FR_PLACE INT NULL, GR VARCHAR(20) NULL, GRB INT NULL, HITW1 INT NULL, '
                   'HITW2 INT NULL, HITW3 INT NULL, PT_RED VARCHAR(20) NULL, PT_ORANGE VARCHAR(20) NULL, '
                   'PT_YELLOW VARCHAR(20) NULL, PT_LIME VARCHAR(20) NULL, PT_GREEN VARCHAR(20) NULL, '
                   'PT_CYAN VARCHAR(20) NULL, PT_AQUA VARCHAR(20) NULL, PT_BLUE VARCHAR(20) NULL, PT_PURPLE '
                   'VARCHAR(20) NULL, PT_PINK VARCHAR(20) NULL, PW_COURSE VARCHAR(20) NULL, RS_KILLS INT NULL, '
                   'RS1 INT NULL, RS2 INT NULL, RS3 INT NULL, SB_KILLS INT NULL, SB_SURVIVAL1 TIME NULL, '
                   'SB_SURVIVAL2 TIME NULL, SB_SURVIVAL3 TIME NULL, SOT VARCHAR( 20) NULL, '
                   'SKYB_KILLS VARCHAR(20) NULL, SKYB_SURVIVAL VARCHAR(20) NULL, SG_KILLS INT NULL, '
                   'SG_SURVIVAL INT NULL, TGTTOS1 VARCHAR(20) NULL, TGTTOS2 VARCHAR(20) NULL, TGTTOS3 VARCHAR( '
                   '20), TGTTOS4 VARCHAR(20) NULL, TGTTOS5 VARCHAR(20) NULL, TGTTOS6 VARCHAR(20) NULL);']
    cur.execute("".join(createQuery))


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

        gameToSql = {"Team": "TEAM",
                     "Ace Race - Time": "AR_TIME",
                     "Ace Race - Place": "AR_PLACE",
                     "Battle Box - Kills": "BB_KILLS",
                     "Battle Box - Wins": "BB_WINS",
                     "Bingo But Fast": "BINGO_FAST",
                     "Lockout Bingo": "LOCK_BINGO",
                     "Build Mart": "BM",
                     "Foot Race - Time": "FR_TIME",
                     "Foot Race - Place": "FR_PLACE",
                     "Grid Runners - Place": "GR",
                     "Grid Runners - Bonus": "GRB",
                     "Hole in the Wall - 1": "HITW1",
                     "Hole in the Wall - 2": "HITW2",
                     "Hole in the Wall - 3": "HITW3",
                     "Parkour Tag - Red": "PT_RED",
                     "Parkour Tag - Orange": "PT_ORANGE",
                     "Parkour Tag - Yellow": "PT_YELLOW",
                     "Parkour Tag - Lime": "PT_LIME",
                     "Parkour Tag - Green": "PT_GREEN",
                     "Parkour Tag - Cyan": "PT_CYAN",
                     "Parkour Tag - Aqua": "PT_AQUA",
                     "Parkour Tag - Blue": "PT_BLUE",
                     "Parkour Tag - Purple": "PT_PURPLE",
                     "Parkour Tag - Pink": "PT_PINK",
                     "Parkour Warrior - Course": "PW_COURSE",
                     "Rocket Spleef - Kills": "RS_KILLS",
                     "Rocket Spleef - 1": "RS1",
                     "Rocket Spleef - 2": "RS2",
                     "Rocket Spleef - 3": "RS3",
                     "Sky Battle - Kills": "SB_KILLS",
                     "Sky Battle - 1": "SB_SURVIVAL1",
                     "Sky Battle - 2": "SB_SURVIVAL2",
                     "Sky Battle - 3": "SB_SURVIVAL3",
                     "Sands Of Time": "SOT",
                     "Skyblockle - Kills": "SKYB_KILLS",
                     "Skyblockle - Survival": "SKYB_SURVIVAL",
                     "SG - Kills": "SG_KILLS",
                     "SG - Survival": "SG_SURVIVAL",
                     "TGTTOS1": "TGTTOS1",
                     "TGTTOS2": "TGTTOS2",
                     "TGTTOS3": "TGTTOS3",
                     "TGTTOS4": "TGTTOS4",
                     "TGTTOS5": "TGTTOS5",
                     "TGTTOS6": "TGTTOS6"}
        if game[0:3] == "MCC":
            NumAndGames.append("MCCNUM")
            NumAndGames.append("PLAYER")
        else:
            NumAndGames.append(gameToSql[str(game)])

    print(len(NumAndGames))

    players = list(df.index.values)
    for i, row in enumerate(df.to_numpy()):
        row = list(row)
        print(len(row))
        row.pop(0)
        createQuery = ['INSERT INTO ', 'MCCDATA (', ', '.join(NumAndGames), ') Values (', "'", header[0], "', '", players[i] ,"'", ',%s)']
        query = "".join(createQuery) % ','.join('?' * len(row))
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
    )

    cur = mydb.cursor(buffered=True)

    cur.execute("CREATE DATABASE IF NOT EXISTS MCC;")
    cur.execute("USE MCC;")
    create_table(cur)
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
