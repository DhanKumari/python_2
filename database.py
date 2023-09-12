import mysql.connector
mydb= mysql.connector.connect(
    host="local host",
    user="root",
    password="",
    database="school"

)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE school")
mycursor.execute("SHOW DATABASE")

for x in mycursor:
    if x=="school":
        print("database is present ")
    else:
        print("not present ")

mycursor.execute("CREATE TABLE Teacher(name varchar(20),dept varchar(30))")

sql="INSERT INTO Teacher(name, dept) VALUES(%s,%s)"
val=[("kannu","etc"),
     ("melvita","comp"),
     ("hrutwa","etc"),
     ("neetal","etc"),
     ("nishika","comp"),
     ("raj","etc"),
     ("musatf","IT"),
     ("keegan","etc"),
]
mycursor.executemany(sql,val)
mydb.commit()

mycursor.execute("CREATE TABLE student(name varchar(20),dept varchar(30))")

sq="INSERT INTO student(name, dept) VALUES(%s,%s)"
va=[("anish","IT"),
     ("kevin","comp"),
     ("namrata","IT"),
     ("vishvas","etc"),
     ("ajay","IT"),
     ("kiran","etc"),
     ("joan","IT"),
     ("ayushi","etc"),
     ("ajaybind","IT"),
     ("karishma","IT"),
     ("jo","IT"),
     ("ayushman","etc"),
]
mycursor.executemany(sql,val)
mydb.commit()
mycursor.execute("CREATE TABLE department(name varchar(20),subject(30))")

sql="INSERT INTO department(name,subject) VALUES(%s,%s)"
val=[("anish","CAS"),
     ("kevin","AC"),
     ("namrata","SOFT COMPUTING "),
     ("vishvas","CNN"),
     ("ajay","CAS"),
     ("kiran","CNN"),
     ("joan","AC"),
     ("ayushi","CNN"),
     ("ajaybind","SOFT COMPUTING"),
     ("karishma","ANN"),
     ("jo","WAS"),
     ("ayushman","CNN"),
]
mycursor.executemany(sql,val)
mydb.commit()

#dispay the tables 
mycursor.execute("SELECT *FROM Teacher WHERE Dept = 'etc'")   ##prints 5 rows  
result1 = mycursor.fetchall()

for x in result1:
    print(x)

mycursor.execute("SELECT *FROM student WHERE Dept = 'IT'") #prints 7 rows
result2 = mycursor.fetchall()

for x in result2:
    print(x)

mycursor.execute("SELECT *FROM department ")  #prints all rows 
result3 = mycursor.fetchall()

for x in result3:
    print(x)
