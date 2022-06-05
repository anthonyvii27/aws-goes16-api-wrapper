class S3Client:
    client = None

    def __init__(self, s3_client):
        self.client = s3_client
