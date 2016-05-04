#!/usr/bin/python

import sqlite3

class Dbtest():
    def connect(self):
        self.dbcon = sqlite3.connect("test.db")
	self.dbcur = self.dbcon.cursor()
    
    def createTable(self):
        self.dbcur.execute("drop table if exists test1")
	self.dbcur.execute("create table test1 ('field1' varchar, 'field2' varchar)")

    def execute(self, sql, parameters):
        print "inserting values: ", parameters
        self.dbcur.execute(sql, parameters)

    def commit(self):
        self.dbcon.commit()

    def close(self):
        self.dbcon.close()

db = Dbtest()
db.connect()
print "...connected"
db.createTable()
value1 = "a"
value2 = "b"
db.execute("insert into test1 (field1, field2) values (?, ?)", (value1, value2))
print "fields inserted"
print "the fields were: %s and % s" % (value1, value2)
db.close()
