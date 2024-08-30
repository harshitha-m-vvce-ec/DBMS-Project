import mysql.connector
a= input("Enter the Database: ")
b=input("Enter the Table name: ")
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="%s"%a)

mycursor = mydb.cursor()
mycursor.execute(f"Create table if not exists {b} ( Fname varchar(200),Lname varchar(200),age integer(100))")
mydb.commit()