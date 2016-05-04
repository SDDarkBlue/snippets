#!/usr/bin/python

import sqlite3
import os
import sys

try:
    os.remove("./test.db")
except:
    print "...File 'test.db' does not exist."

# create a database
con = sqlite3.connect("./test.db")
cursor = con.cursor()
# create a table
cursor.execute("create table 'testtable' ('field1', 'field2')")
con.commit()

# insert data in table
cursor.execute("insert into testtable values ('1', '2')")
cursor.execute("insert into testtable values ('BANG', 'BANG')")
con.commit()

# fetch data from table
cursor.execute("select * from testtable")
rows = cursor.fetchall()
print "fetched rows:"
for row in rows:
    print row

# fetch more data
cursor.execute("select * from testtable where field1=?", ["BANG"])
rows = cursor.fetchall()
print "fetched rows when looking for BANG:"
for row in rows:
    print row

# clean up
con.close()
os.remove("./test.db")
