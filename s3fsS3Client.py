import s3fs

from s3Client import S3Client
from exceptions import ValueNotProvidedError


class S3fsS3Client(S3Client):
    def __init__(self):
        super().__init__()
        self.client = s3fs.S3FileSystem(anon=True)

    def authenticate(self, access_key, secret_key):
        self.client = s3fs.S3FileSystem(anon=False, key=access_key, secret=secret_key)

    def list_buckets(self):
        pass

    def list_files(self, bucket_name):
        if not bucket_name:
            raise ValueNotProvidedError(message='bucket name not provided')

        # if bucket_name == "remoto" or bucket_name == self.local_bucket:
        #     # Abre a pasta e lista os arquivos sem usar o s3fs/boto3
        #     pass

        try:
            files = self.client.ls(f's3://{bucket_name}')

            if len(files) == 0:
                print(f'The bucket {bucket_name} hasn\'\t files to list')
                return

            for file in files:
                print(file)

        except Warning as err:
            print(f'Error: {err}')
