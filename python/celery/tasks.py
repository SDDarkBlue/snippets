from celery import Celery

app = Celery('tasks', backend='redis://localhost', broker='redis://localhost:6379/0')
app.config_from_object('celeryconfig')

@app.task
def add(x, y):
    return x + y
