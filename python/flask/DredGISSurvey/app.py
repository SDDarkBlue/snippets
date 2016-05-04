from flask import Flask, request, g, connect_db, jsonify
import pyodbc


# configuration
DEBUG = True
connection_url = 'mysql+pyodbc://user:pass@host:123/db'

app = Flask(__name__)
app.config.from_object(__name__)

@app.before_request
def before_request():
    cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=172.16.203.38:1434;DATABASE=DredGIS;UID=bart_aelterman;PWD=iF0cus@Value')
    g.db = cnxn

@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db', None)
    if db is not None:
        db.close()

@app.route('/')
def show_survey():
    survey_info = [
        {
        'name': 'DredGIS',
        'description': 'Onderzoek naar bodemvervuiling op baggergronden',
        'start date': '1997-05-28'
        },
        {
        'name': 'FloodGIS',
        'description': 'Onderzoek naar bodemvervuiling in overstromingsgebieden',
        'start date': '2007-11-06'
        }
    ]
    return jsonify(surveys=survey_info)

if __name__ == '__main__':
    app.run()
