import numbers
import os
from datetime import datetime

import numpy as np

from .awsS3Api import AwsS3Api
from .exceptions import ValueNotProvidedError
from .utils import get_hour, get_year, convert_to_date, convert_to_datetime, convert_date_to_day_of_year, \
    is_valid_datetime, is_valid_date

INITIAL_YEAR = 2018

class AwsS3ApiGoes16(AwsS3Api):
    __product_list = ['ABI-L1b-RadF', 'ABI-L1b-RadC', 'ABI-L1b-RadM', 'ABI-L2-ACHAC', 'ABI-L2-ACHAF', 'ABI-L2-ACHAM',
                      'ABI-L2-ACHTF', 'ABI-L2-ACHTM', 'ABI-L2-ACMC', 'ABI-L2-ACMF', 'ABI-L2-ACMM', 'ABI-L2-ACTPC',
                      'ABI-L2-ACTPF', 'ABI-L2-ACTPM', 'ABI-L2-ADPC', 'ABI-L2-ADPF', 'ABI-L2-ADPM', 'ABI-L2-AODC',
                      'ABI-L2-AODF', 'ABI-L2-CMIPC', 'ABI-L2-CMIPF', 'ABI-L2-CMIPM', 'ABI-L2-CODC', 'ABI-L2-CODF',
                      'ABI-L2-CPSC', 'ABI-L2-CPSF', 'ABI-L2-CPSM', 'ABI-L2-CTPC', 'ABI-L2-CTPF', 'ABI-L2-DMWC',
                      'ABI-L2-DMWF', 'ABI-L2-DMWM', 'ABI-L2-DSIC', 'ABI-L2-DSIF', 'ABI-L2-DSIM', 'ABI-L2-DSRC',
                      'ABI-L2-DSRF', 'ABI-L2-DSRM', 'ABI-L2-FDCC', 'ABI-L2-FDCF', 'ABI-L2-LSTC', 'ABI-L2-LSTF',
                      'ABI-L2-LSTM', 'ABI-L2-LVMPC', 'ABI-L2-LVMPF', 'ABI-L2-LVMPM', 'ABI-L2-LVTPC', 'ABI-L2-LVTPF',
                      'ABI-L2-LVTPM', 'ABI-L2-MCMIPC', 'ABI-L2-MCMIPF', 'ABI-L2-MCMIPM', 'ABI-L2-RRQPEF', 'ABI-L2-RSRC',
                      'ABI-L2-RSRF', 'ABI-L2-SSTF', 'ABI-L2-TPWC', 'ABI-L2-TPWF', 'ABI-L2-TPWM', 'ABI-L2-VAAF',
                      'GLM-L2-LCFA', 'SUVI-L1b-Fe093', 'SUVI-L1b-Fe131', 'SUVI-L1b-Fe171', 'SUVI-L1b-Fe195',
                      'SUVI-L1b-Fe284', 'SUVI-L1b-He303']

    def __init__(self, s3_client_name='s3fs'):
        super().__init__(s3_client_name, remote_bucket='noaa-goes16')
        self.__product = 'GLM-L2-LCFA'
        self.__initial_date = ''
        self.__due_date = ''
        self.__data_variable = 'event_energy'
        self.__lat_long_coords = dict(zip(['n_lat', 's_lat', 'w_lon', 'e_lon'], ['', '', '', '']))

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

    @property
    def lat_long_coords(self):
        return self.__lat_long_coords

    @product.setter
    def product(self, product_name):
        if not product_name:
            raise ValueNotProvidedError(message='product_name parameter not provided')

        upper_product_name = product_name.upper()
        is_valid = upper_product_name in self.__product_list
        if not is_valid:
            raise Warning('Invalid product. Check the valid product list in '
                          'https://github.com/anthonyvii27/aws-goes16-api-wrapper/docs/valid_products.md or use the '
                          'method list_products')

        self.__product = product_name

    @initial_date.setter
    def initial_date(self, date):
        if not date:
            raise ValueNotProvidedError(message='date parameter not provided')

        is_valid = is_valid_datetime(date)
        if not is_valid:
            raise Warning('The provided date has a invalid format. The accepted format is yyyy-mm-dd HH')

        self.__initial_date = convert_to_datetime(date)

    @due_date.setter
    def due_date(self, date):
        if not date:
            raise ValueNotProvidedError(message='date parameter not provided')

        is_valid = is_valid_datetime(date)
        if not is_valid:
            raise Warning('The provided date has a invalid format. The accepted format is yyyy-mm-dd HH')

        formatted_date = convert_to_datetime(date)

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

    @lat_long_coords.setter
    def lat_long_coords(self, coords):
        if not isinstance(coords, dict):
            raise Warning('The entered format is invalid. The accepted format is a dictionary with the structure: {'
                          '\'n_lat\': value, \'s_lat\': value, \'w_lon\': value, \'e_lon\': value}')

        for coord_type, value in coords.items():
            if not value or not isinstance(value, numbers.Number):
                raise Warning(f'The value entered for the attribute {coord_type} is invalid')

        self.__lat_long_coords = coords

    def authenticate(self, access_key, secret_key):
        """
        Allows performing authentication using the defined s3 bucket and thus making requests to private buckets to
        which the logged-in user has access

        :param access_key: AWS access key credential
        :param secret_key: AWS secret key credential
        :return: void
        """
        self._s3_client.authenticate(access_key, secret_key)

    def list_buckets(self):
        """
        Displays the list of available buckets using the defined s3 client

        :return: void
        """
        self._s3_client.list_buckets(self.remote_bucket, self.local_bucket)

    def list_bucket_files(self, bucket_name=''):
        """
        Displays the list of files present inside the defined bucket, which can be local or remote

        :param bucket_name: S3 bucket name
        :return: void
        """
        if bucket_name == 'local' or bucket_name == self.local_bucket:
            self._s3_client.list_bucket_files(bucket_name, self.local_bucket)
            return

        self._s3_client.list_bucket_files(self.remote_bucket, self.local_bucket)

    def list_products(self):
        """
        Displays the list of NOAA GOES 16 products

        :return: void
        """
        print(f'----------- PRODUCTS -----------\nSee more: https://docs.opendata.aws/noaa-goes16/cics-readme.html')
        for product in self.__product_list:
            print(f'-  {product}')

    def get_file_metadata(self, filename, datetime):
        """
        Get the specified file's metadata
        :param filename: File name to download
        :param datetime: Datetime in format yyyy-mm-dd HH
        :return: object
        """
        is_valid = is_valid_datetime(datetime)
        if not is_valid:
            raise Warning('The "datetime" parameter has an invalid format. The accepted format is "yyyy-mm-dd HH"')

        formatted_date = convert_to_datetime(datetime)
        year = get_year(formatted_date)
        hour = get_hour(formatted_date)
        day_of_year = convert_date_to_day_of_year(formatted_date)

        try:
            return self._s3_client.get_file_metadata(
                path=f'{self.remote_bucket}/{self.__product}/{year}/{day_of_year}/{hour}',
                filename=filename
            )
        except Warning as err:
            print(f'An error has occurred: {err}')

    def get_file(self, datetime, filename):
        """
        Download the specified file to the defined local bucket

        :param filename: File name to download
        :param datetime: Datetime in format yyyy-mm-dd HH
        :return: void
        """
        # is_valid = is_valid_datetime(datetime)
        # if not is_valid:
        #     raise Warning('The "datetime" parameter has an invalid format. The accepted format is "yyyy-mm-dd HH"')

        formatted_date = convert_to_datetime(datetime)
        year = get_year(formatted_date)
        hour = get_hour(formatted_date)
        day_of_year = convert_date_to_day_of_year(formatted_date)

        try:
            self._s3_client.get_file(
                self.local_bucket,
                path=f'{self.remote_bucket}/{self.__product}/{year}/{day_of_year}/{hour}',
                filename=filename,
                coords=self.__lat_long_coords,
                netcdf_data_variable=self.data_variable,
                product_name=self.__product
            )
        except Warning as err:
            print(f'An error has occurred: {err}')

    def get_all_files_one_day(self, date, logs=True):
        """
            Download the specified file to the defined local bucket

            :param logs:
            :param date: Datetime in format yyyy-mm-dd HH
            :return: void
        """
        is_valid = is_valid_date(date)
        if not is_valid:
            raise Warning('The "date" parameter has an invalid format. The accepted format is "yyyy-mm-dd"')

        formatted_date = convert_to_date(date)
        year = get_year(formatted_date)
        day_of_year = convert_date_to_day_of_year(formatted_date)

        for i in range(24):
            files = np.array(
                self._s3_client.list_files_by_path(path=f'noaa-goes16/{self.__product}/{year}/{day_of_year}/{i}'))

            try:
                for file in files:
                    filename = file.split('/')[-1]
                    if logs:
                        print(f'Downloading file: [{day_of_year}/{year} - {i}] {filename}')
                    self.get_file(filename=filename, datetime=f'{date} {i}')
            except ValueError:
                pass

    def get_all_files_from_the_last(self, logs=True):
        years = os.listdir(self.local_bucket)
        if not years:
            years.append(str(INITIAL_YEAR))
            os.mkdir(f'{self.local_bucket}/{INITIAL_YEAR}')

        last_year = int(max(years))

        days_in_the_years = os.listdir(f'{self.local_bucket}/{last_year}')
        if not days_in_the_years:
            days_in_the_years.append('098')

        last_day = max(days_in_the_years)

        qty_days_in_the_year = 365

        if (last_year % 4 == 0 and last_year % 100 != 0) or (last_year % 400 == 0):
            qty_days_in_the_year += 1

        print('Preparing to download files...')
        for i in range(int(last_day), qty_days_in_the_year + 1):
            day_num = str(i)
            day_num = day_num.rjust(3, '0')

            date = datetime.strptime(f'{last_year}-{day_num}', '%Y-%j').strftime('%Y-%m-%d')
            self.get_all_files_one_day(date, logs=logs)
