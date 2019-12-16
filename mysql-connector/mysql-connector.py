import mysql.connector

mydb = mysql.connector.connect(
    host = "jeongmupark.com",
    user = "pantagruel",
    passwd = "-",
    database = "pantagruel"
)

my_cursor = mydb.cursor()
my_cursor.execute("SHOW TABLES")
for db in my_cursor:
    print(db)