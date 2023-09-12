import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", user="root", password="", database="school"
)

mycursor = mydb.cursor()

"""
mycursor.execute(
    "CREATE TABLE IF NOT EXISTS Teacher(name varchar(20),dept varchar(30))"
)

sql1 = "INSERT INTO Teacher(name, dept) VALUES(%s,%s)"
val1 = [
    ("kannu", "etc"),
    ("melvita", "comp"),
    ("hrutwa", "etc"),
    ("neetal", "etc"),
    ("nishika", "comp"),
    ("raj", "etc"),
    ("musatf", "IT"),
    ("keegan", "etc"),
]
mycursor.executemany(sql1, val1)
mydb.commit()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS student(name varchar(20),dept varchar(30))"
)

sql2 = "INSERT INTO student(name, dept) VALUES(%s,%s)"
val2 = [
    ("anish", "IT"),
    ("kevin", "comp"),
    ("namrata", "IT"),
    ("vishvas", "etc"),
    ("ajay", "IT"),
    ("kiran", "etc"),
    ("joan", "IT"),
    ("ayushi", "etc"),
    ("ajaybind", "IT"),
    ("karishma", "IT"),
    ("jo", "IT"),
    ("ayushman", "etc"),
]
mycursor.executemany(sql2, val2)
mydb.commit()

mycursor.execute(
    "CREATE TABLE IF NOT EXISTS department(name varchar(20),subject VARCHAR(30))"
)

sql3 = "INSERT INTO department(name,subject) VALUES(%s,%s)"
val3 = [
    ("anish", "CAS"),
    ("kevin", "AC"),
    ("namrata", "SOFT COMPUTING "),
    ("vishvas", "CNN"),
    ("ajay", "CAS"),
    ("kiran", "CNN"),
    ("joan", "AC"),
    ("ayushi", "CNN"),
    ("ajaybind", "SOFT COMPUTING"),
    ("karishma", "ANN"),
    ("jo", "WAS"),
    ("ayushman", "CNN"),
]
mycursor.executemany(sql3, val3)
mydb.commit()"""


# dispay the tables
mycursor.execute("SELECT *FROM Teacher LIMIT 5")  ##prints 1st  5 rows
result1 = mycursor.fetchall()

print("\n")
for x in result1:
    print(x)

mycursor.execute("SELECT *FROM student LIMIT 7")  # prints 1st 7 rows
result2 = mycursor.fetchall()
print("\n")
for x in result2:
    print(x)

mycursor.execute("SELECT *FROM department ")  # prints all rows
result3 = mycursor.fetchall()
print("\n")
for x in result3:
    print(x)

