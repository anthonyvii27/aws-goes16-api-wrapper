from inspect import signature
import boto3
from botocore import UNSIGNED
from botocore.client import Config
from s3Client import S3Client

class Boto3S3Client(S3Client):
    def __init__():
        super().__init__(boto3.client('s3', config=Config(signature_version=UNSIGNED)))