import s3fs
import os

from s3Client import S3Client
from exceptions import ValueNotProvidedError


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

        print(f'----------- LOCAL -----------\n- {local_bucket_path}\n')
        print('----------- REMOTE -----------')

        if remote_bucket_path:
            print(f'- {remote_bucket_path}')

        # TODO - Implements bucket listing by s3fs
        if self.__is_authenticated:
            pass

    def list_files(self, bucket_name, local_bucket_path):
        if not bucket_name:
            raise ValueNotProvidedError(message='bucket name not provided')

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

    def get_file(self, remote_bucket_path, filename):
        self.__client.get(remote_bucket_path, filename)
