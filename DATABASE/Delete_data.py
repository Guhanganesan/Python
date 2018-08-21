import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)
mycursor = mydb.cursor()
sql = "delete from details where name='guhan'"
mycursor.execute(sql)
mydb.commit()
print(mycursor.rowcount, "record(s) deleted")

Result:
   1 record(s) deleted
