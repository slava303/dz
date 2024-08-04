import os
import logging
from collections import namedtuple
import argparse

# Настройка логирования в файл
logging.basicConfig(filename='errors_6.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Определяем namedtuple для хранения информации о файлах и каталогах
FileInfo = namedtuple('FileInfo', ['name', 'extension', 'is_directory', 'parent_directory'])

def collect_directory_info(directory_path):
    # Список для хранения информации о файлах и каталогах
    directory_contents = []

    # Проходим по всем элементам в указанной директории
    for entry in os.scandir(directory_path):
        if entry.is_file():
            name, extension = os.path.splitext(entry.name)
            is_directory = False
        elif entry.is_dir():
            name = entry.name
            extension = None
            is_directory = True
        else:
            continue  # Игнорируем другие типы

        parent_directory = os.path.basename(directory_path)
        file_info = FileInfo(name=name, extension=extension, is_directory=is_directory, parent_directory=parent_directory)
        directory_contents.append(file_info)

        # Логируем информацию о файле или каталоге
        logging.info(f"Обнаружен: {file_info}")

    return directory_contents

def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description='Соберите информацию о содержимом директории.')
    parser.add_argument('directory', type=str, help='Путь до директории на ПК')

    args = parser.parse_args()

    # Проверяем, существует ли указанная директория
    if not args.directory.strip():  # Проверка на пустую строку
        logging.error("Путь до директории не может быть пустым.")
        print("Ошибка: Путь до директории не может быть пустым.")
        return

    if not os.path.isdir(args.directory):
        logging.error(f"Указанная директория не существует: {args.directory}")
        print(f"Ошибка: Указанная директория не существует: {args.directory}")
        return

    # Собираем информацию о содержимом директории
    directory_info = collect_directory_info(args.directory)

    # Выводим информацию на экран
    for info in directory_info:
        print(info)

if __name__ == "__main__":
    main()
