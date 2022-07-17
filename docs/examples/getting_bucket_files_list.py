from awsgoes16.src.awsS3ApiGoes16 import AwsS3ApiGoes16

api_goes = AwsS3ApiGoes16()

# USING THE LOCAL BUCKET ALIAS = 'local'
api_goes.list_bucket_files(bucket_name='local')

# REMOTE BUCKET
api_goes.list_bucket_files()
