#!/usr/bin/python
import pyodbc

cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=localhost;DATABASE=testdb;UID=me;PWD=pass')
cursor = cnxn.cursor()
cursor.execute("select user_id, user_name from users")
rows = cursor.fetchall()
for row in rows:
    print row.user_id, row.user_name
