import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)
mycursor = mydb.cursor()
sql = "insert into details (name, age, mobile) values ('Guhan', '28',979181)"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#----------------------------------------------------

Result:-

1 record inserted.
