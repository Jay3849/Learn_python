import mysql.connector


import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    username="root",
    password="Root",
    port=3306,
    database="pymysql"
    )

mycurosr = mydb.cursor()