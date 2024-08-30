import mysql.connector
b=input("Enter the database name: ")
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="%s" % b)
mycursor = mydb.cursor()
g=input("Enter the Table to be Dropped: ")
mycursor.execute("drop table %s"%g)
mydb.commit()