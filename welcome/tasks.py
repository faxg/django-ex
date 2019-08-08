from celery import shared_task
import os


@shared_task
def getInfo():
    result = {
        "redis_uri": os.getenv("redis_uri"),
        "redis_password": os.getenv("password")
    }
    return result

