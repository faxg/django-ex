from celery import shared_task
import os
from project.settings import *


@shared_task
def getInfo():
    result = {
        "CELERY_BROKER_URL": CELERY_BROKER_URL,
    }
    return result

