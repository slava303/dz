# Создайте функцию, которая запрашивает числовые данные от
# пользователя до тех пор, пока он не введёт целое или вещественное число.
# Обрабатывайте не числовые данные как исключения.
import logging
import argparse

# Настройка логирования в файл
logging.basicConfig(filename='errors_7.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def get_numeric_input(user_input):
    try:
        # Попытка преобразовать ввод в число
        if '.' in user_input:
            number = float(user_input)
        else:
            number = int(user_input)
        return number  # Возвращаем число, если преобразование прошло успешно
    except ValueError:
        # Логируем ошибку, если ввод не является числом
        logging.error(f"Некорректный ввод из аргументов: {user_input}")
        print("Ошибка: Ввод должен быть числом.")
        return None

def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description='Запрос числовых данных.')
    parser.add_argument('number', type=str, help='Целое или вещественное число')

    args = parser.parse_args()

    # Получаем числовой ввод

    number = get_numeric_input(args.number)

    if number is not None:
        print(f"Вы ввели число: {number}")

if __name__ == "__main__":
    main()
