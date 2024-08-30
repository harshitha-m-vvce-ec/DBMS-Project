import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")

mycursor=mydb.cursor()

mycursor.execute("delete from pptable where fname='xyz'")

mydb.commit()