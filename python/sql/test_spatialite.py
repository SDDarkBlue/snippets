import sqlite3

db = sqlite3.connect('spatialtest.db')
db.enable_load_extension(True)
db.execute("SELECT load_extension('mod_sptialite');")
cur = db.cursor()
