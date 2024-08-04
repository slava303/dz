import re
from datetime import datetime, timedelta
import logging

# Настройка логирования
logging.basicConfig(filename="errors_4.log",level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

def get_date_from_text(text):
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

    # Регулярное выражение для проверки формата
    pattern = r'(\d+)-й (понедельник|вторник|среда|четверг|пятница|суббота|воскресенье) (января|февраля|марта|апреля|мая|июня|июля|августа|сентября|октября|ноября|декабря)'
    match = re.match(pattern, text)

    if not match:
        logging.error(f"Неверный формат: {text}")
        return None

    week_number = int(match.group(1))
    weekday_name = match.group(2)
    month_name = match.group(3)

    # Получаем номер месяца и дня недели
    month = months[month_name]
    weekday = weekdays[weekday_name]

    # Получаем текущий год
    current_year = datetime.now().year

    # Находим нужную дату
    first_day_of_month = datetime(current_year, month, 1)
    days_to_add = (weekday - first_day_of_month.weekday() + 7) % 7
    first_weekday = first_day_of_month + timedelta(days=days_to_add)

    # Находим нужный по порядку день недели
    target_date = first_weekday + timedelta(weeks=week_number - 1)

    return target_date

# Пример использования
text_input = input("Введите дату в формате '1-й четверг ноября,3-я среда мая' ")
date_result = get_date_from_text(text_input)

if date_result:
    print(f"Преобразованная дата: {date_result.strftime('%Y-%m-%d')}")
