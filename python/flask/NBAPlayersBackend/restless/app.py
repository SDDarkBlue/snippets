import flask
import flask.ext.sqlalchemy
from sqlalchemy.ext.hybrid import hybrid_property
import flask.ext.restless
from time import strptime
from datetime import date
import csv
import os

# Clear database if it exists
try:
    os.unlink('/tmp/test.db')
except:
    pass

# Create the Flask application
app = flask.Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)

# Create models
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    height = db.Column(db.Float)

    @hybrid_property
    def avg_stats(self):
        tstats = GameStats.query.filter_by(player_id=self.id).all()
        if len(tstats) > 0:
            points = [x.points for x in tstats]
            minutes = [x.minutes for x in tstats]
            return {'points_per_game': 1.0 * sum(points) / len(tstats),
                    'minutes_per_game': 1.0 * sum(minutes) / len(tstats)
                   }
        else:
            return None

class GameStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player = db.relationship('Player', backref=db.backref('stats', lazy='dynamic'))
    minutes = db.Column(db.Float)
    points = db.Column(db.Integer)

# Create all database tables
db.create_all()

# Load players
datafile = 'data/nba_players.csv'
with open(datafile) as f:
    pid = 1
    reader = csv.reader(f, delimiter='\t')
    header = reader.next()
    for row in reader:
        name, height, number, position, team, weight = row
        p = Player(id=pid, name=name, height=height)
        db.session.add(p)
        pid += 1
    db.session.commit()

# Load stats
datafile = 'data/NBA-Player-Sample-BoxScore-Dataset-cleaned.csv'
with open(datafile) as f:
    sid = 1
    reader = csv.reader(f, delimiter=',')
    header = reader.next()
    for row in reader:
        name, sdate, minutes, points = [row[2], row[1], row[6], row[21]]
        time = strptime(sdate, '%d-%m-%Y')
        sdate = date(time.tm_year, time.tm_mon, time.tm_mday)
        qresults = Player.query.filter_by(name=name).all()
        if len(qresults) != 1:
            print 'Could not find unique player with name {0}'.format(name)
        else:
            player = qresults[0]
            gs = GameStats(player=player, date=sdate, minutes=minutes, points=points)
            db.session.add(gs)
    db.session.commit()

# Create Flask-restless API manager
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename>
manager.create_api(Player, methods=['GET'], results_per_page=-1, include_columns=['name', 'height', 'stats', 'avg_stats'])
manager.create_api(GameStats, allow_functions=True)

# Start the Flask loop
app.run()
