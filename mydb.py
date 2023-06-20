import mysql.connector

database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "rootrootroot"
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE django_crm")

print("All done!")