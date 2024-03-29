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
    def list_bucket_files(self, bucket_name, local_bucket_path):
        pass

    @abstractmethod
    def list_files_by_path(self, path):
        pass

    @abstractmethod
    def get_file_metadata(self, path, filename):
        pass

    @abstractmethod
    def get_file(self, local_bucket, filename, path, coords, netcdf_data_variable, product_name):
        pass
