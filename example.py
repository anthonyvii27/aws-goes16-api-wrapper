from awsS3ApiGoes16 import AwsS3ApiGoes16

apiGoes = AwsS3ApiGoes16()
apiGoes.product = 'GLM-L2-LCFA'

print(f'Remote bucket: {apiGoes.remote_bucket}')
print(f'Local bucket: {apiGoes.local_bucket}')
print(f'Product: {apiGoes.product}')

apiGoes.initial_date = '2019-04-08'
apiGoes.due_date = '2019-05-08'

print(f'Initial date: {apiGoes.initial_date}')
print(f'Due date: {apiGoes.due_date}')

print('\n')

apiGoes.local_bucket = '/Users/testing'
print(f'New local bucket: {apiGoes.local_bucket}')

apiGoes.local_bucket = '/'
print(f'New local bucket from alias: {apiGoes.local_bucket}')

print('\n')

bucket_list = apiGoes.s3_client.list_buckets(apiGoes.remote_bucket, apiGoes.local_bucket)

print('\n')

file_list = apiGoes.s3_client.list_files('noaa-goes16/GLM-L2-LCFA/2019/098/18', apiGoes.local_bucket)