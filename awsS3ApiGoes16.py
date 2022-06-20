from awsS3Api import AwsS3Api
from exceptions import ValueNotProvidedError
from utils import convert_to_date, convert_date_to_day_of_year, get_year, get_hour, is_valid_date


class AwsS3ApiGoes16(AwsS3Api):
    def __init__(self, s3_client_name='s3fs'):
        super().__init__(s3_client_name, remote_bucket='noaa-goes16')
        self.__product = 'GLM-L2-LCFA'
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
        if not product_name:
            raise ValueNotProvidedError(message='product_name parameter not provided')

        self.__product = product_name

    @initial_date.setter
    def initial_date(self, date):
        if not date:
            raise ValueNotProvidedError(message='date parameter not provided')

        is_valid = is_valid_date(date)
        if not is_valid:
            raise Warning('Invalid format')

        self.__initial_date = convert_to_date(date)

    @due_date.setter
    def due_date(self, date):
        if not date:
            raise ValueNotProvidedError(message='date parameter not provided')

        is_valid = is_valid_date(date)
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
        if not value:
            raise ValueNotProvidedError(message='value parameter not provided')

        self.__data_variable = value

    def authenticate(self, access_key, secret_key):
        self._s3_client.authenticate(access_key, secret_key)

    def list_buckets(self):
        self._s3_client.list_buckets(self.remote_bucket, self.local_bucket)

    def list_files(self):
        self._s3_client.list_files(self.remote_bucket, self.local_bucket)

    def get_file(self, filename, datetime):
        is_valid = is_valid_date(datetime)
        if not is_valid:
            raise Warning('The "datetime" parameter has an invalid format. The accepted format is "yyyy-mm-dd HH"')

        formatted_date = convert_to_date(datetime)
        year = get_year(formatted_date)
        hour = get_hour(formatted_date)
        day_of_year = convert_date_to_day_of_year(formatted_date)

        try:
            self._s3_client.get_file(f'{self.remote_bucket}/{self.__product}/{year}/{day_of_year}/{hour}/{filename}',
                                     filename)
        except Warning as err:
            print(f'An error has occurred: {err}')
