import s3fs
from s3Client import S3Client


class S3fsS3Client(S3Client):
    def __init__(self):
        super().__init__()
        self.client = s3fs.S3FileSystem(anon=True)

    def authenticate(self, access_key, secret_key):
        self.client = s3fs.S3FileSystem(anon=False, key=access_key, secret=secret_key)

    def list_buckets(self):
        pass

    def list_files(self):
        pass
