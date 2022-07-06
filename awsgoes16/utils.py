from datetime import datetime
import re


def is_valid_date(str_date):
    """
    Checks if the entered date is valid

    :param str_date: Date in string format
    :return: bool
    """
    return bool(re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$', str_date))


def is_valid_datetime(str_datetime):
    """
    Checks if the entered datetime is valid

    :param str_datetime: Date in string format
    :return: bool
    """
    return bool(re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])\s([0-2]\d)$', str_datetime))


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


def get_year(date):
    """
    Get the year of a date in datetime format

    :param date: Date in datetime format
    :return: int
    """
    return date.year


def get_hour(date):
    """
    Get the hour of a date in datetime format

    :param date: Date in datetime format
    :return: int
    """
    return date.hour
