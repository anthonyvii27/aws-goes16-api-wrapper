import s3fs
from s3Client import S3Client


class S3fsS3Client(S3Client):
    def __init__(self):
        super().__init__(s3fs.S3FileSystem(anon=True))
