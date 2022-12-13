import random
from time import sleep
from rich.console import Console

console = Console()
print('Скачивание файлов...')
tasks = [f'Файл {n}' for n in range(1, 7)]
with console.status('[bold green]Скачивание файлов...[/bold green]') as status:
    while tasks:
        task = tasks.pop(0)
        sleep(random.uniform(1, 5))
        console.log(f'{task} успешно загружен!')

print('Файлы успешно загружены на ваш компьютер.')
