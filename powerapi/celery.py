from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "powerapi.settings")

app = Celery("powerapi")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


from celery.schedules import crontab

app.conf.beat_schedule = {
    "update-drive-io-1": {
        "task": "powerapi.tasks.update_drive_io",
        "schedule": 60.0,  # Every 60 seconds
        "args": (
            "ca60b0c8-268b-a342-9037-33a0c848a2e4",
        ),  # You can pass the drive name here
    },
    "update-drive-io-2": {
        "task": "powerapi.tasks.update_drive_io",
        "schedule": 60.0,
        "args": ("57710fcf-1a53-7b4b-8c46-508b4edab623",),
    },
    "update-drive-io-3": {
        "task": "powerapi.tasks.update_drive_io",
        "schedule": 60.0,
        "args": ("d74294d8-daab-c445-a38a-f122353e1f59",),
    },
    "update-cpu-power": {
        "task": "powerapi.tasks.update_cpu_power",
        "schedule": 60.0,
        "args": ("Intel(R) Xeon(R) CPU E5-2630 v4 @ 2.20GHz",),
    }
}
