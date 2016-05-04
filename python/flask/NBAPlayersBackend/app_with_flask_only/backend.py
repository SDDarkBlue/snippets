# -*- coding: utf-8 -*-

from contextlib import closing
import sqlite3
import csv
from flask import Flask, request, session, g, redirect, url_for, abort, flash, jsonify

DATABASE = "nba_players.db"
DEBUG = True
SECRET_KEY = "development key"
USERNAME = "admin"
PASSWORD = "default"

app = Flask(__name__)
app.config.from_object(__name__)

def init_db():
    with closing(connect_db()) as db:
        with app.open_resource("schema.sql") as f:
	    db.cursor().executescript(f.read())
            import_data(db, 'nba_players.csv')
	db.commit()

def import_data(dbcon, infile):
    with open(infile) as f:
        cur = dbcon.cursor()
        pid = 1
        reader = csv.reader(f, delimiter='\t')
        header = reader.next()
        for row in reader:
            name, height, number, position, team, weight = row
            cur.execute('insert into players values (?, ?, ?, ?, ?, ?, ?)', [pid, name, height, number, position, team, weight])
            pid += 1
        dbcon.commit()

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route("/")
def show_players():
    cur = g.db.execute('select * from players order by id desc')
    result = [{'pid':row[0], 'name':row[1], 'height':row[2], 'number':row[3], 'position':row[4], 'team':row[5], 'weight':row[6]} for row in cur.fetchall()]
    return jsonify(results=result)

if __name__ == "__main__":
    app.run()

