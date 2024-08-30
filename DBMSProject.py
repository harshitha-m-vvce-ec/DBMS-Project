import mysql.connector
x="y"
while True:
    if(x=="y"):
        a = int(input("1 To Create DataBase\n2 To Show all DataBase\n3 To Create Table\n4 To Insert Values into Table\n5 To Show content of the table\n6 To Delete the content of the table\n7 To Drop table\n8 To Drop/Delete DataBase\nEnter your choice: "))
        if(a==1):
            mydb = mysql.connector.connect(host="localhost", user="root", password="")
            b=input("Enter the database name: ")
            mycursor = mydb.cursor()
            mycursor.execute("Create database if not exists %s" %b)


        elif(a==2):
            mydb = mysql.connector.connect(host="localhost", user="root", password="")
            mycursor = mydb.cursor()
            mycursor.execute("Show databases")
            for  db in mycursor:
               print(db)


        elif(a==3):
           mydb = mysql.connector.connect(host="localhost", user="root", password="",database = "%s"%b)
           mycursor = mydb.cursor()
           c=input("Enter the table name: ")
           mycursor.execute("Create table if not exists %s( Fname varchar(200),Lname varchar(200),age integer(100))" %c)

        elif(a==4):
            mydb = mysql.connector.connect(host="localhost", user="root", password="",database = "%s"%b)
            mycursor = mydb.cursor()
            p="y"
            while True:

                if(p=='y'):
                    z = input("Enter the table name: ")
                    r = input("Enter the FirstName: ")
                    q = input("Enter the LastName: ")
                    t = input("Enter the age: ")
                    # mycursor.execute("Insert into tempdb values (%s, %s, %s)" %r %q %t)
                    sqlform = (f"Insert into {z} values(%s, %s, %s)")
                    names = (r , q, t)
                    mycursor.execute(sqlform , names)

                else:
                    break
                p = input("*********Do you want to Enter Few more values? y/n***********")
            mydb.commit()


        elif(a==5):
            mydb = mysql.connector.connect(host="localhost", user="root", password="",database = "%s"%b)
            mycursor = mydb.cursor()
            mycursor.execute("Select * from %s"%c)
            myresults = mycursor.fetchall()
            for row in myresults:
                print(row)

        elif(a==6):
            mydb = mysql.connector.connect(host="localhost", user="root", password="",database = "%s"%b)
            mycursor = mydb.cursor()

            e=input("Enter the Fname: ")
            val=(c,e)
            mycursor.execute("delete from &s where Fname=%s", val)
            mydb.commit()

        elif(a==7):
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="%s" % b)
            mycursor = mydb.cursor()
            g=input("Enter the Table to be Dropped: ")
            mycursor.execute("drop table %s"%g)
            mydb.commit()

        elif(a==8):
            mydb = mysql.connector.connect(host="localhost", user="root", password="", database="")
            mycursor = mydb.cursor()
            h=input("Enter teh DataBase to be deleted: ")
            mycursor.execute("drop database %s"%h)
            mydb.commit()
        else:
            print("invalid input!!!!!")
    else:
        break
    x = input("Do you want to continue? y/n")