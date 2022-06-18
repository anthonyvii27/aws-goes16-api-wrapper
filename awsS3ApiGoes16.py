from awsS3Api import AwsS3Api
from utils import convert_to_date
import re


class AwsS3ApiGoes16(AwsS3Api):
    def __init__(self, s3_client_name='s3fs'):
        super().__init__(s3_client_name, remote_bucket='noaa-goes16')
        self.__product = ''
        self.__initial_date = ''
        self.__due_date = ''
        self.__data_variable = ''

    @property
    def product(self):
        return self.__product

    @property
    def initial_date(self):
        return self.__initial_date

    @property
    def due_date(self):
        return self.__due_date

    @property
    def data_variable(self):
        return self.__data_variable

    @product.setter
    def product(self, product_name):
        self.__product = product_name

    @initial_date.setter
    def initial_date(self, date):
        is_valid = re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$', date)
        if not is_valid:
            raise Warning('Invalid format')
        self.__initial_date = convert_to_date(date)

    @due_date.setter
    def due_date(self, date):
        is_valid = re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01])$', date)
        if not is_valid:
            raise Warning('Invalid format')

        formatted_date = convert_to_date(date)

        if not self.__initial_date:
            self.__due_date = formatted_date
        else:
            if self.__initial_date > formatted_date:
                raise Warning('The due date entered is earlier than the initial date')
            else:
                self.__due_date = formatted_date

    @data_variable.setter
    def data_variable(self, value):
        self.__data_variable = value
