import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="")

mycursor = mydb.cursor()
a= input("Enter the database name: ")
mycursor.execute("Create database if not exists %s"%a)