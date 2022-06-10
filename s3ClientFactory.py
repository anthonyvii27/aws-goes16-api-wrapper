from boto3S3Client import Boto3S3Client
from s3fsS3Client import S3fsS3Client


class S3ClientFactory:
    client_dictionary = {"boto3": Boto3S3Client, "s3fs": S3fsS3Client}

    @staticmethod
    def create(client_name):
        client = S3ClientFactory.client_dictionary[client_name]
        return client()
