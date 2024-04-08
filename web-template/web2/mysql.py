import mysql.connecter

mydb = mysql.connecter.connect(
    host = "localhost",
    user = "root",
    password = "",
    )
print(mydb)
