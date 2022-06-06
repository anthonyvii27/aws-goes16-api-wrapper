import boto3
from botocore import UNSIGNED
from botocore.client import Config
from s3Client import S3Client


class Boto3S3Client(S3Client):
    def __init__(self):
        super().__init__()
        self.client = boto3.client('s3', config=Config(signature_version=UNSIGNED))

    def authenticate(self, access_key, secret_key):
        self.client = boto3.client('s3', aws_access_key_id=access_key, aws_secret_access_key=secret_key)

    def list_buckets(self):
        pass

    def list_files(self):
        pass
