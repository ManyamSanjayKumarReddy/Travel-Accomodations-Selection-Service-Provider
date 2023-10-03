import mysql.connector

# User Your own User name and Password to connect with your Database
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'root',

)

# Prepare cursor object
cursorObject = dataBase.cursor()

# Create a database

cursorObject.execute("CREATE DATABASE worldxplorer")

print("All Done!")