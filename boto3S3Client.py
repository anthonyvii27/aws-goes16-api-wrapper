import boto3
from botocore import UNSIGNED
from botocore.client import Config

from s3Client import S3Client
from exceptions import ValueNotProvidedError


class Boto3S3Client(S3Client):
    def __init__(self):
        super().__init__()
        self.client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    def authenticate(self, access_key, secret_key):
        self.client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    def list_buckets(self):
        pass

    def list_files(self, bucket_name):
        if not bucket_name:
            raise ValueNotProvidedError(message='bucket name not provided')

        # if bucket_name == "remoto" or bucket_name == self.local_bucket:
        #     # Abre a pasta e lista os arquivos sem usar o s3fs/boto3
        #     pass

        try:
            for key in self.client.list_objects_v2(Bucket=bucket_name, Prefix='', Delimiter='')['Contents']:
                print(key['Key'])

        except Warning as err:
            print(f'Error: {err}')
