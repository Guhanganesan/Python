import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)
mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE details (name varchar(30), age varchar(30), mobile varchar(30))")

