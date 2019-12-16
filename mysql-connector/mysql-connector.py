import mysql.connector

mydb = mysql.connector.connect(
    host = "jeongmupark.com",
    user = "pantagruel",
    passwd = "^pass0912_",
)

print(mydb)