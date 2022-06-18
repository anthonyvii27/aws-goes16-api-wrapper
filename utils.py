from datetime import datetime


def convert_to_date(str_date):
    return datetime.strptime(str_date, '%Y-%m-%d')


def convert_date_to_day_of_year(date):
    return date.strftime('%j')
