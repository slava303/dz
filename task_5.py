import re
import argparse
from datetime import datetime, timedelta
import logging

# Настройка логирования в файл
logging.basicConfig(filename='errors_5.log', level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def get_date_from_text(week_number, weekday, month):
    # Определяем месяцы и дни недели
    months = {
        "января": 1,
        "февраля": 2,
        "марта": 3,
        "апреля": 4,
        "мая": 5,
        "июня": 6,
        "июля": 7,
        "августа": 8,
        "сентября": 9,
        "октября": 10,
        "ноября": 11,
        "декабря": 12
    }

    weekdays = {
        "понедельник": 0,
        "вторник": 1,
        "среда": 2,
        "четверг": 3,
        "пятница": 4,
        "суббота": 5,
        "воскресенье": 6
    }

    # Преобразование текстовых значений в числовые
    if isinstance(month, str):
        month = months.get(month, int(month))  # Если это строка, преобразуем в число
    if isinstance(weekday, str):
        weekday = weekdays.get(weekday, int(weekday))  # Если это строка, преобразуем в число

    # Получаем текущий год
    current_year = datetime.now().year

    # Если параметры не заданы, используем текущие значения
    if month is None:
        month = datetime.now().month
    if weekday is None:
        weekday = datetime.now().weekday()
    if week_number is None:
        week_number = 1  # По умолчанию берем первую неделю

    # Находим первую дату месяца
    first_day_of_month = datetime(current_year, month, 1)

    # Находим первый нужный день недели в месяце
    days_to_add = (weekday - first_day_of_month.weekday() + 7) % 7
    first_weekday = first_day_of_month + timedelta(days=days_to_add)

    # Находим нужный по порядку день недели
    target_date = first_weekday + timedelta(weeks=week_number - 1)

    # Проверяем, не вышли ли мы за пределы месяца
    if target_date.month != month:
        logging.error(f"Дата выходит за пределы месяца: неделя {week_number}, день {weekday}, месяц {month}")
        return None

    return target_date

def main():
    # Настройка аргументов командной строки
    parser = argparse.ArgumentParser(description='Преобразование текстового ввода в дату.')
    parser.add_argument('--week', type=int, help='Номер недели (по умолчанию 1)')
    parser.add_argument('--weekday', type=str, help='День недели (например, "понедельник" или "0" для понедельника)')
    parser.add_argument('--month', type=str, help='Месяц (например, "января" или "1" для января)')

    args = parser.parse_args()

    # Получаем дату из аргументов
    date_result = get_date_from_text(args.week, args.weekday, args.month)

    if date_result:
        print(f"Преобразованная дата: {date_result.strftime('%Y-%m-%d')}")
    else:
        logging.error("Не удалось преобразовать дату.")

if __name__ == "__main__":
    main()
