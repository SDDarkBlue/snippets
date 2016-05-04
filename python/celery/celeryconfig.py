from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-60-seconds': {
        'task': 'tasks.add',
        'schedule': timedelta(minutes=1),
        'args': (10, 20)
    },
}

CELERY_TIMEZONE = 'Europe/London'
