import os
#import redis
import urlparse
import sqlite3
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from jinja2 import Environment, FileSystemLoader

class DBLayer():
    def __init__(self):
        pass

    def sql_output_2_json(self, sql_rows):
	results = []
	for row in sql_rows:
	    row_in_json = {'id': row[0], 'value1': row[1].encode('utf-8')}
	    results.append(row_in_json)
	return str(results)

    def get_all(self):
        print 'fetching all stuff from the db'
        con = sqlite3.connect('./test.db')
	cursor = con.cursor()
        cursor.execute('select * from table1;')
	rows = cursor.fetchall()
	con.close()
	return self.sql_output_2_json(rows)

    def get_by_id(self, idnr):
        con = sqlite3.connect('./test.db')
	cursor = con.cursor()
        cursor.execute('select * from table1 where id=?;', [idnr])
	rows = cursor.fetchall()
	con.close()
	return self.sql_output_2_json(rows)

class Shortly(object):

    def __init__(self, config):
        #self.redis = redis.Redis(config['redis_host'], config['redis_port'])
	template_path = os.path.join(os.path.dirname(__file__), 'templates')
	self.jinja_env = Environment(loader=FileSystemLoader(template_path), autoescape=True)
	self.url_map = Map([
	    Rule('/', endpoint='new_url'),
	])
	self.db = DBLayer()

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
	return Response(t.render(context), mimetype='text/html')

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
	try:
	    endpoint, values = adapter.match()
	    return getattr(self, 'on_' + endpoint)(request, **values)
	except HTTPException, e:
	    return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
	response = self.dispatch_request(request)
	return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

    def on_new_url(self, request):
	idnr = request.args.get('id', '')
	if idnr == "":
	    results = self.db.get_all()
	else:
	    results = self.db.get_by_id(idnr)
	return Response(results)


def create_app(redis_host='localhost', redis_port=6379, with_static=True):
    app = Shortly({
	'redis_host': redis_host,
	'redis_port': redis_port
    })
    if with_static:
	app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
	    '/static': os.path.join(os.path.dirname(__file__), 'static')
	})
    return app

if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
