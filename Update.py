import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password="", database="pp")

mycursor = mydb.cursor()

sqlform="Insert into employeedata( Fname ,Lname ,age ) values(%s, %s, %s)"

names=[("pratiksha","HL",20),("prajwal","gujjar",21),("mayur","v",23),("nidhi","shastry",20),("nikhil","r",25)]

mycursor.executemany(sqlform, names)
mydb.commit()