import boto3
from botocore import UNSIGNED
from botocore.client import Config

from s3Client import S3Client
from exceptions import ValueNotProvidedError


class Boto3S3Client(S3Client):
    def __init__(self):
        super().__init__()
        self.is_authenticated = False
        self.client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    def authenticate(self, access_key, secret_key):
        try:
            self.client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)
            self.is_authenticated = True
        except Warning as err:
            print(f'Error: {err}')

    def list_buckets(self, remote_bucket_path, local_bucket_path):
        print(f'----------- LOCAL -----------\n- {local_bucket_path}\n')
        print('----------- REMOTE -----------\n')

        if remote_bucket_path:
            print(f'- {remote_bucket_path}')

        if self.is_authenticated:
            remote_buckets = self.client.list_buckets()
            print(f'- {remote_buckets}')

    def list_files(self, bucket_name, local_bucket_path):
        if not bucket_name:
            raise ValueNotProvidedError(message='bucket name not provided')

        if bucket_name == 'remoto' or bucket_name == local_bucket_path:
            pass

        try:
            for key in self.client.list_objects_v2(
                    Bucket=bucket_name,
                    Prefix='',
                    Delimiter=''
            )['Contents']:
                print(key['Key'])

        except Warning as err:
            print(f'Error: {err}')
