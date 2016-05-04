import psycopg2
import sys

con = None

try:
    con = psycopg2.connect(database='bird_tracking', user='bart_aelterman')
    cur = con.cursor()
    cur.execute('SELECT version()')
    ver = cur.fetchone()
    print ver

except psycopg2.DatabaseError, e:
    print 'Error {0}'.format(e)
    sys.exit(-1)

finally:
    if con:
        con.close()
