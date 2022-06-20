from datetime import datetime
import re


def is_valid_date(date):
    return re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\s([0-2]\d)$', date)


def convert_to_date(str_datetime):
    return datetime.strptime(str_datetime, '%Y-%m-%d %H')


def convert_date_to_day_of_year(date):
    return date.strftime('%j')


def get_year(date):
    return date.year


def get_hour(date):
    return date.hour
