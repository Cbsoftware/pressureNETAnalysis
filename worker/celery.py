from __future__ import absolute_import

import os

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

from tasks.aggregator import app

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-30-seconds': {
        'task': 'tasks.aggregator.BlockHandler',
        'schedule': timedelta(seconds=10),
    },
}

CELERY_TIMEZONE = 'UTC'
