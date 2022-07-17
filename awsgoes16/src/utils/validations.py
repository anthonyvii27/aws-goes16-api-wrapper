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
