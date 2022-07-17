from datetime import datetime


def convert_to_date(str_datetime):
    """
    Converts a string date to date

    :param str_datetime: Convert the date in string format to date
    :return: date
    """
    return datetime.strptime(str_datetime, '%Y-%m-%d')


def convert_to_datetime(str_datetime):
    """
    Converts a string date to datetime

    :param str_datetime: Convert the date in string format to datetime
    :return: datetime
    """
    return datetime.strptime(str_datetime, '%Y-%m-%d %H')


def convert_date_to_day_of_year(date):
    """
    Convert a date to day in year

    :param date: Date in datetime format
    :return: string
    """
    return date.strftime('%j')
