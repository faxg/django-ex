#!/usr/bin/env python
import os
import sys
from django.core.management import execute_from_command_line


if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")

    # start local Celery worker
    os.system("./start-celery-worker.sh &")


    execute_from_command_line(sys.argv)
