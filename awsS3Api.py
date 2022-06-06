from abc import ABC
from s3ClientFactory import S3ClientFactory


class AwsS3Api(ABC):
    remote_bucket = ""
    local_bucket = ""

    def __init__(self, s3_client_name):
        self.s3_client = S3ClientFactory.create(s3_client_name)

    def set_remote_bucket(self, bucket_name):
        self.remote_bucket = bucket_name

    def set_local_bucket(self, bucket_name):
        self.local_bucket = bucket_name
