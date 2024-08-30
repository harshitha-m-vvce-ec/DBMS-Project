import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")

mycursor=mydb.cursor()

mycursor.execute("Select * from pptable")
myresults=mycursor.fetchall()

for row in myresults:
    print(row)