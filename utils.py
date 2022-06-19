from datetime import datetime


def convert_to_date(str_datetime):
    return datetime.strptime(str_datetime, '%Y-%m-%d %H')


def convert_date_to_day_of_year(date):
    return date.strftime('%j')


def get_year(date):
    return date.year


def get_hour(date):
    return date.hour
