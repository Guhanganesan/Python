import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="pythondb"
)
mycursor = mydb.cursor()
mycursor.execute("select * from details")
myresult = mycursor.fetchall()
for x in myresult:
  print(x
  
Result:-
('Guhan', '28', '979181')

