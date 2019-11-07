from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'workshop.settings')
app = Celery('workshop')
app.config_from_object('django.conf:settings')
