from abc import ABC, abstractmethod


class S3Client(ABC):
    def __init__(self, s3_client):
        self.client = s3_client

    @abstractmethod
    def authenticate(self):
        pass

    @abstractmethod
    def list_buckets(self):
        pass

    @abstractmethod
    def list_files(self):
        pass
