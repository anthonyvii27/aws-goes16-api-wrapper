from abc import ABC, abstractmethod
from .s3ClientFactory import S3ClientFactory
from .exceptions import ValueNotProvidedError
import os


class AwsS3Api(ABC):
    def __init__(self, s3_client_name, remote_bucket='', local_bucket=os.getcwd()):
        self._s3_client = S3ClientFactory.create(s3_client_name)
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

        if bucket_name == '/':
            self.__local_bucket = os.getcwd()
        else:
            self.__local_bucket = bucket_name

    @abstractmethod
    def authenticate(self, access_key, secret_key):
        pass

    @abstractmethod
    def list_buckets(self):
        pass

    @abstractmethod
    def list_bucket_files(self, bucket_name):
        pass

    @abstractmethod
    def get_file_metadata(self, filename, datetime):
        pass

    @abstractmethod
    def get_file(self, filename, datetime):
        pass
