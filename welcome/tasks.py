from celery import shared_task
import os
from project.settings import *
import time
from datetime import datetime


@shared_task
def getInfo():
    result = {
        "CELERY_BROKER_URL": CELERY_BROKER_URL,
    }
    return result

@shared_task
def sleep(seconds):
    time.sleep(seconds)
    return {"was_sleeping_for": seconds}
