import mysql.connector
import mysql.vendor

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


