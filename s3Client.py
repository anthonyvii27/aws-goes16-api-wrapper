from abc import ABC, abstractmethod


class S3Client(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def authenticate(self, access_key, secret_key):
        pass

    @abstractmethod
    def list_buckets(self, remote_bucket_path, local_bucket_path):
        pass

    @abstractmethod
    def list_files(self, bucket_name, local_bucket_path):
        pass

    @abstractmethod
    def get_file(self, remote_bucket_path, filename):
        pass

    @abstractmethod
    def get_file_metadata(self, remote_bucket_path, filename):
        pass
