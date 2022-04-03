import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Iamc00l!rsb897h4",
    database="MCC"
)

mycursor = mydb.cursor()



for x in mycursor:
    print(x)

mydb.commit()
mydb.close()

def set_ranboo_data():
    mycursor.execute()