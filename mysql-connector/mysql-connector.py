import mysql.connector

mydb = mysql.connector.connect(
    host = "",
    user = "",
    passwd = "",
)

print(mydb)