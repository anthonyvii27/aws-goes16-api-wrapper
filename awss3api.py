class AWSS3API:
    remote_bucket = ""
    local_bucket = ""

    def __init__(self, s3_client="s3_client"):
        self.s3_client = s3_client
