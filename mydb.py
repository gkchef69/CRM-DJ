import mysql.connector

dataBase = mysql.connector.connect(host='localhost', user='root', passwd = 'pass123', port = 8080)

cursor = dataBase.cursor()

cursor.execute("CREATE DATABASE costworkcrm")

print("done")