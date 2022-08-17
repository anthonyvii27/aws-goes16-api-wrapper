import s3fs
import os
import xarray as xr

from awsgoes16.src.s3Client import S3Client
from awsgoes16.src.exceptions import ValueNotProvidedError
from awsgoes16.src.utils.converters import get_xy_from_latlon, calc_latlon

PRODUCT_LIST_WITH_LAT_LON = ['ABI-L2-DMWC', 'ABI-L2-DMWF', 'ABI-L2-DMWM', 'ABI-L2-DSRC', 'ABI-L2-DSRF',
                             'ABI-L2-DSRM', 'ABI-L2-RSRC', 'ABI-L2-RSRF']

PRODUCT_LIST_WITH_EVENT_LAT_LONG = ['GLM-L2-LCFA']

PRODUCT_LIST_WITHOUT_COORDS = ['SUVI-L1b-Fe093', 'SUVI-L1b-Fe131', 'SUVI-L1b-Fe171', 'SUVI-L1b-Fe195',
                               'SUVI-L1b-Fe284', 'SUVI-L1b-He303']


class S3fsS3Client(S3Client):
    def __init__(self):
        super().__init__()
        self.__is_authenticated = False
        self.__client = s3fs.S3FileSystem(anon=True)

    def authenticate(self, access_key, secret_key):
        if not access_key:
            raise ValueNotProvidedError(message='access_key parameter not provided')

        if not secret_key:
            raise ValueNotProvidedError(message='secret_key parameter not provided')

        try:
            self.__client = s3fs.S3FileSystem(anon=False, key=access_key, secret=secret_key)
            self.__is_authenticated = True
        except Warning:
            print('unable to authenticate')

    def list_buckets(self, remote_bucket_path, local_bucket_path):
        if not remote_bucket_path:
            raise ValueNotProvidedError(message='remote_bucket_path parameter not provided')

        if not local_bucket_path:
            raise ValueNotProvidedError(message='local_bucket_path parameter not provided')

        print(f'----------- LOCAL -----------\n-  {local_bucket_path}\n')
        print('----------- REMOTE -----------')

        if remote_bucket_path:
            print(f'-  {remote_bucket_path}')

        # TODO - Implements bucket listing by s3fs
        if self.__is_authenticated:
            pass

    def list_bucket_files(self, bucket_name, local_bucket_path):
        if not bucket_name:
            raise ValueNotProvidedError(message='bucket_name not provided')

        if not local_bucket_path:
            raise ValueNotProvidedError(message='local_bucket_path parameter not provided')

        if bucket_name == 'local' or bucket_name == local_bucket_path:
            print(f'----------- FILES -----------\nPath: {local_bucket_path}\n')
            dir_list = os.listdir(local_bucket_path)
            for file in dir_list:
                print(f'-  {file}')
            return

        try:
            print(f'----------- FILES -----------\nPath: s3://{bucket_name}\n')
            files = self.__client.ls(f's3://{bucket_name}')

            if len(files) == 0:
                print(f'the bucket {bucket_name} hasn\'\t files to list')
                return

            for file in files:
                print(f'-  {file}')

        except Warning as err:
            print(f'Error: {err}')

    def list_files_by_path(self, path):
        files = self.__client.ls(path)
        return files

    def get_file_metadata(self, path, filename):
        try:
            with self.__client.open(f'{path}/{filename}', 'rb') as file:
                return file.metadata()

        except Warning as err:
            print(f'Error: {err}')

    def get_file(self, local_bucket, filename, path, coords, netcdf_data_variable, product_name):
        if not filename:
            raise ValueNotProvidedError('Error: Filename not provided')

        if not path:
            raise ValueNotProvidedError('Error: Path not provided')

        if not coords['n_lat']:
            raise ValueNotProvidedError('It is necessary to provide the value referring to north latitude: n_lat')

        if not coords['s_lat']:
            raise ValueNotProvidedError('It is necessary to provide the value referring to south latitude: s_lat')

        if not coords['e_lon']:
            raise ValueNotProvidedError('It is necessary to provide the value referring to east longitude: e_lon')

        if not coords['w_lon']:
            raise ValueNotProvidedError('It is necessary to provide the value referring to west latitude: w_lon')

        path_to_save_file = f'{local_bucket}/{path.split("/")[2]}/{path.split("/")[3]}'
        if not os.path.isdir(path_to_save_file):
            os.makedirs(path_to_save_file)

        with self.__client.open(f'{path}/{filename}', 'rb') as file:
            ds = xr.open_dataset(file)
            ds = (ds['event_energy'].where(
                (ds['event_lat'] >= coords['s_lat']) & (ds['event_lat'] <= coords['n_lat']) &
                (ds['event_lon'] >= coords['w_lon']) & (ds['event_lon'] <= coords['e_lon']),
                drop=True))

            df = ds.to_dataframe()
            df.drop(df.columns[4:-1], axis=1, inplace=True)
            df.drop(df.columns[0], axis=1, inplace=True)
            df.rename(columns={'event_time_offset': 'time',
                               'event_lat': 'lat',
                               'event_lon': 'lon',
                               'event_energy': 'energy'},
                      inplace=True)
            df.set_index('time', inplace=True)

            df.to_csv(f'{path_to_save_file}/{filename[:-3]}.csv')
            file.close()
