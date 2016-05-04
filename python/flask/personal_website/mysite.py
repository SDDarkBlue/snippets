from __future__ import with_statement
from contextlib import closing
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_bootstrap import Bootstrap
import os
import sys
from blogparser.classes import BlogParser

# Configuration
DATABASE = './tmp/mysite.db'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


# Create app
app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)

# Initialize the database
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql') as f:
	    db.cursor().executescript(f.read())
	db.commit()

# Connect to database
def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.before_request
def before_request():
    g.db = connect_db()

@app.teardown_request
def teardown_request(exception):
    g.db.close()

@app.route('/')
def show_entries():
    cur = g.db.execute('select name, description, url from projects order by id desc')
    projects = [dict(name=row[0], description=row[1], url=row[2]) for row in cur.fetchall()]
    bp = BlogParser()
    parameters = {'max-results': 5}
    url = 'http://bioinformatics-man.blogspot.com/feeds/posts/default' 
    try:
	blogposts = bp.search_article(url, parameters)
    except Exception:
        blogposts = None
    return render_template('show_projects.html', projects=projects, blogposts=blogposts)

@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
	abort(401)
    g.db.execute('insert into projects (name, description, url) values (?, ?, ?)', [request.form['name'], request.form['description'], request.form['url']])
    g.db.commit()
    flash('New project added successfully.')
    return redirect(url_for('show_entries'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
	if request.form['username'] != app.config['USERNAME']:
	    error = 'Invalid username or password'
	elif request.form['password'] != app.config['PASSWORD']:
	    error = 'Invalid username or password'
	else:
	    session['logged_in'] = True
	    flash('Welcome {0}'.format(request.form['username']))
	    return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()
