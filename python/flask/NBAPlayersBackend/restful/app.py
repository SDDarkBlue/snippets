from flask import Flask, jsonify
import flask.ext.sqlalchemy
from flask.ext.restful import Resource, Api, fields, marshal_with
from time import strptime
from datetime import date
import csv
import os

# Clear database if it exists
os.unlink('/tmp/test.db')

# Create the Flask application
app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db = flask.ext.sqlalchemy.SQLAlchemy(app)
api = Api(app)

# Create models
class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Unicode)
    height = db.Column(db.Float)

    def serialize(self):
        return {
            'name': self.name,
            'height': self.height
        }

class GameStats(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    player = db.relationship('Player', backref=db.backref('stats', lazy='dynamic'))
    minutes = db.Column(db.Float)
    points = db.Column(db.Integer)

    def serialize(self):
        return {
            'date': self.date.isoformat(),
            'player_id': self.player_id,
            'minutes': self.minutes,
            'points': self.points
        }

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

# Create Restful Resources

class PlayerRes(Resource):
    pfields = {'name': fields.String, 'height': fields.Raw}
    @marshal_with(pfields)
    def get(self, player_id):
        p = Player.query.get(player_id)
        return {'name': p.name, 'height': p.height}

class PlayerListRes(Resource):
    def get(self):
        players = Player.query.all()
        return jsonify(players=[p.serialize() for p in players])

class GameStatsRes(Resource):
    #gfields = {'player_id': fields.Integer, 'points': fields.Integer, 'minutes': fields.Raw, 'date': fields.Raw}
    def get(self):
        gs = GameStats.query.all()
        return jsonify(stats=[s.serialize() for s in gs])

api.add_resource(PlayerRes, '/api/player/<string:player_id>')
api.add_resource(PlayerListRes, '/api/player')
api.add_resource(GameStatsRes, '/api/game_stats')

# Start the Flask loop
app.run()
