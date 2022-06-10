import s3fs

from s3Client import S3Client
from exceptions import ValueNotProvidedError


class S3fsS3Client(S3Client):
    def __init__(self):
        super().__init__()
        self.is_authenticated = False
        self.client = s3fs.S3FileSystem(anon=True)

    def authenticate(self, access_key, secret_key):
        try:
            self.client = s3fs.S3FileSystem(anon=False, key=access_key, secret=secret_key)
            self.is_authenticated = True
        except Warning:
            print('unable to authenticate')

    def list_buckets(self, remote_bucket_path, local_bucket_path):
        print(f'----------- LOCAL -----------\n- {local_bucket_path}\n')
        print('----------- REMOTE -----------\n')

        if remote_bucket_path:
            print(f'- {remote_bucket_path}')

        # TODO - Implements bucket listing by s3fs
        if self.is_authenticated:
            pass

    def list_files(self, bucket_name, local_bucket_path):
        if not bucket_name:
            raise ValueNotProvidedError(message='bucket name not provided')

        # TODO - Implements local file management
        if bucket_name == 'local' or bucket_name == local_bucket_path:
            pass

        try:
            files = self.client.ls(f's3://{bucket_name}')

            if len(files) == 0:
                print(f'the bucket {bucket_name} hasn\'\t files to list')
                return

            for file in files:
                print(file)

        except Warning as err:
            print(f'Error: {err}')
