from abc import ABC
from s3ClientFactory import S3ClientFactory
from exceptions import ValueNotProvidedError


class AwsS3Api(ABC):
    def __init__(self, s3_client_name, remote_bucket='', local_bucket=''):
        self.s3_client = S3ClientFactory.create(s3_client_name)
        self.__remote_bucket = remote_bucket
        self.__local_bucket = local_bucket

    @property
    def remote_bucket(self):
        return self.__remote_bucket

    @property
    def local_bucket(self):
        return self.__local_bucket

    @remote_bucket.setter
    def remote_bucket(self, bucket_name):
        if not bucket_name:
            raise ValueNotProvidedError(message='bucket name not provided')
        self.__remote_bucket = bucket_name

    @local_bucket.setter
    def local_bucket(self, bucket_name):
        if not bucket_name:
            raise ValueNotProvidedError(message='bucket name not provided')
        self.__local_bucket = bucket_name
