from celery import shared_task
from .models import Outputs

from celery.decorators import periodic_task
from celery.task.schedules import crontab
import requests
import subprocess
from time import sleep


@shared_task
def get_linux_data():
    url = "http://127.0.0.1:8000/commands/"
    data = requests.get(url).json()
    cmd = data[-1]['cmd']
    repetition = data[-1]['repetition']
    gap = data[-1]['gap']

    output = ""

    for i in range(int(repetition)):
        p = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        output += p.stdout
        sleep(int(gap))

    out1 = Outputs()
    out1.op = output
    out1.save()


@periodic_task(run_every=(crontab(minute='*/1')))
def get_linux_current():
    get_linux_data.delay()
