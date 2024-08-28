import os
import time
directory = '.'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory)
        filetime = os.path.getmtime(directory)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        file_size = os.path.getsize(directory)
        parent_dir = os.path.dirname(directory)
        print(
            f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {file_size} байт, '
            f'Время изменения: {formatted_time}, Родительская директория: {parent_dir}')