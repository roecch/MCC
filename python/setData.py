import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iamc00l!rsb897h4",
    database="MCC"
)

cur = mydb.cursor(buffered=True)

for x in cur:
    print(x)

mydb.commit()
mydb.close()


def set_ranboo_data():
    query = "REPLACE INTO RANBOO (MCCNUM, COLOR, ACERACE_TIME, ACERACE_PLACE, BB_KILLS, BB_WINS, HITW, PT_HUNTER, PT_RUNNER, " \
            "SB_SURVIVAL, SB_KILLS, SOT_SOLO, SG_SURVIVAL, SG_KILLS, TGTTOS_1, TGTTOS_2, TGTTOS_3, TGTTOS_4, TGTTOS_5, TGTTOS_6) " \
            "VALUES (15, 'pink', '06:21:20', 9, 6, null, null, null, null, null, null, null, null, '21:37:37', 1, 414, null, null, null, null)"
    cur.execute()
