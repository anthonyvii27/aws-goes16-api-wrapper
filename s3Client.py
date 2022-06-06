from abc import ABC, abstractmethod


class S3Client(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def authenticate(self, access_key, secret_key):
        pass

    @abstractmethod
    def list_buckets(self):
        pass

    @abstractmethod
    def list_files(self):
        pass
