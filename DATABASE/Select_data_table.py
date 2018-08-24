import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="abi"
)
mycursor = mydb.cursor()
sql=  "select * from details where mobile='8757851'"
try:
  mycursor.execute(sql)
  results=mycursor.fetchall()
  for row in results:
       name=row[0]
       age=row[1]
       mobile=row[2]
       print(name,age,mobile)
except:
       print("Error")
