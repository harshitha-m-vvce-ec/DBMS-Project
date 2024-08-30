import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="")
mycursor = mydb.cursor()
a=input("Enter the Table to be Dropped: ")
mycursor.execute("drop table %s"%a)
mydb.commit()