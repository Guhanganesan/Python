# Download mysql connector module from github
#https://github.com/mysql/mysql-connector-python
# Go to lib/mysql copy this file and pase it in Create_database.py area in your PC
#Ex: C:\Users\Server\PycharmProjects\String\Create_database.py
# Import mysql\connector folder

#-----------------------------------------

import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd=""
)
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE pythondb")

# Go and check localhost/phpmyadmin page


