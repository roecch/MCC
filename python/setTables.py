import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iamc00l!rsb897h4",
    database="MCC"
)

cur = mydb.cursor(buffered=True)

all_players = ['5up', 'antfrost', 'asnazum', 'awesamdude', 'badboyhalo', 'bbpaws', 'bitzel', 'captainpuffy', 'captainsparklez', 'connoreatspants',
               'cubfan135', 'cxlvxn', 'dantdm', 'dethridge', 'dream', 'drgluon', 'elainaexe', 'eret', 'f1nn5ter', 'falsesymmetry', 'florianfluke',
               'fruitberries', 'fundy', 'fwhip', 'geenelly', 'geminitay', 'georgenotfound', 'gizzygazza', 'goodtimeswithscar', 'grain', 'graser10',
               'hbomb94', 'ihascupquake', 'iicbunnyx', 'ijevin', 'illumina', 'inthelittlewood', 'iskall85', 'itsjustoriah', 'jackmanifold',
               'jacksucksatlife', 'jamescharles', 'jameskii', 'jamesturner', 'jcthecaster', 'jeromeasf', 'jestanii', 'joeygraceffa', 'karacorvus',
               'karljacobs', 'katherineelizabeth', 'kingburren', 'kontuz', 'krinios', 'krtzzy', 'kryticzeuz', 'laurenzside', 'ldshadowlady', 'ludwig',
               'marielitai', 'mefs', 'michaelmcchill', 'minimuka', 'nettyplays', 'nihachu', 'pearlbytez', 'pearlescentmoon', 'petezahhut', 'philza',
               'plumbella', 'pokimane', 'ponk', 'prestonplayz', 'punz', 'purpled', 'quackity', 'quig', 'rafessor', 'ranboo', 'rendog', 'ripmika',
               'roguskii', 'rtgame', 'ryguyrocky', 'sapnap', 'sb737', 'scotgrisworld', 'seapeekay', 'shubble', 'skeppy', 'slimecicle', 'smajor1995',
               'smallishbeans', 'sneegsnag', 'solidaritygaming', 'spifey', 'steph0sims', 'strawburry17', 'sylvee', 'tankmatt', 'tapl', 'technoblade',
               'theorionsound', 'tommyinnit', 'toxxicsupport', 'tubbo', 'vapekit', 'vgumiho', 'vikkstar123', 'vixella', 'voiceoverpete', 'wilbur',
               'wisp', 'wolv21', 'yammyxox', 'yeetdaisie'];

cur.execute("SELECT TABLE_NAME from information_schema.tables where TABLE_SCHEMA = 'mcc'")
playerExists = cur.fetchall()

for player in all_players:

    if (player,) not in playerExists:
        createQuery = ['CREATE TABLE IF NOT EXISTS ', player, '(MCCNUM VARCHAR(20), COLOR VARCHAR(20), ACERACE_TIME TIME, ACERACE_PLACE INT, BB_KILLS INT, '
                                                              'BB_WINS INT, BINGO VARCHAR(20), BM VARCHAR(20), GR VARCHAR(20), HITW TIME, PT_HUNTER VARCHAR'
                                                              '(20), PT_RUNNER VARCHAR(20), PW_FIRST VARCHAR(20), PW_COURSE VARCHAR(20), SB_SURVIVAL TIME, '
                                                              'SB_KILLS INT, SOT_SOLO VARCHAR(20), SKYBLOCKE VARCHAR(20), SG_SURVIVAL INT, SG_KILLS INT, '
                                                              'TGTTOS_1 INT, TGTTOS_2 INT, TGTTOS_3 INT, TGTTOS_4 INT, TGTTOS_5 INT, TGTTOS_6 INT);']
        query = "".join(createQuery)
        cur.execute(query)

        for num in range(20):
            setAllNull = ['INSERT INTO ', player,
                          ' VALUES (', str(num + 1), ', null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, null, '
                                                     'null, null, null, null, null, null, null, null);']
            query = "".join(setAllNull)
            cur.execute(query)

for x in cur:
    print(x)

mydb.commit()
mydb.close()
