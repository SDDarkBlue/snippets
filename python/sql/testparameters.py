#!/usr/bin/python

#import psycopg2
import sqlite3

#con = psycopg2.connect(host="localhost", database="testpgdb", user="pygresuser", password="pygresuser")
con = sqlite3.connect("test.db")
print "...connected"
cur = con.cursor()
cur.execute("drop table if exists test1")
cur.execute("create table test1 ('field1' varchar, 'field2' varchar)")

cur.execute("delete from test1 where field1='a'")
con.commit()
value1 = "a"
value2 = "b"
cur.execute("insert into test1 (field1, field2) values (?, ?)", (value1, value2))
con.commit()
print "values inserted"
con.close()
