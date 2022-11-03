import random
from time import sleep
from rich.progress import track


def do_step(step):
    sleep(random.uniform(0.1, 1))


for step in track(range(100), description='Загрузка Windows...'):
    do_step(step)
