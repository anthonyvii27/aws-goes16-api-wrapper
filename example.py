from awsS3ApiGoes16 import AwsS3ApiGoes16

apiGoes = AwsS3ApiGoes16()

apiGoes.product = 'GLM-L2-LCFA'

print(f'Remote bucket: {apiGoes.remote_bucket}')
print(f'Local bucket: {apiGoes.local_bucket}')
print(f'Product: {apiGoes.product}')

print('\n\n')

bucket_list = apiGoes.s3_client.list_buckets(apiGoes.remote_bucket, apiGoes.local_bucket)

print('\n\n')

apiGoes.local_bucket = '/Users/testing'
print(f'New local bucket: {apiGoes.local_bucket}')

apiGoes.local_bucket = '/'
print(f'New local bucket from alias: {apiGoes.local_bucket}')

file_list = apiGoes.s3_client.list_files('noaa-goes16/GLM-L2-LCFA/2019/098/18', apiGoes.local_bucket)

# apiGoes.s3_client.get_file('noaa-goes16/GLM-L2-LCFA/2019/098/18/OR_GLM-L2-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc', 'OR_GLM-L2-LCFA_G16_s20190981800000_e20190981800200_c20190981800229.nc')
