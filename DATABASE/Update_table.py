import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)
mycursor = mydb.cursor()
sql = "update details set mobile=9867 where name='guhan'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) affected")

Result:-
1 record(s) affected

name  age  mobile
Guhan 28    9867
